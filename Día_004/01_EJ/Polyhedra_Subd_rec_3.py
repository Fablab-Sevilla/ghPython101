import Rhino
import Rhino.Geometry as rg

# ----------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------

def model_tol():
    try:
        return Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance
    except:
        return 1e-6

def _poly_area2d(pts):
    # signed area (CCW > 0)
    s = 0.0
    n = len(pts)
    for i in range(n):
        j = (i + 1) % n
        s += pts[i].X * pts[j].Y - pts[j].X * pts[i].Y
    return 0.5 * s

def _is_convex(a, b, c, ccw, eps):
    cross = (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X)
    return (cross > eps) if ccw else (cross < -eps)

def _pt_in_tri_2d(p, a, b, c, eps):
    # barycentric test in 2D
    v0 = (c.X - a.X, c.Y - a.Y)
    v1 = (b.X - a.X, b.Y - a.Y)
    v2 = (p.X - a.X, p.Y - a.Y)

    dot00 = v0[0]*v0[0] + v0[1]*v0[1]
    dot01 = v0[0]*v1[0] + v0[1]*v1[1]
    dot02 = v0[0]*v2[0] + v0[1]*v2[1]
    dot11 = v1[0]*v1[0] + v1[1]*v1[1]
    dot12 = v1[0]*v2[0] + v1[1]*v2[1]

    denom = dot00 * dot11 - dot01 * dot01
    if abs(denom) < eps:
        return False
    invd = 1.0 / denom
    u = (dot11 * dot02 - dot01 * dot12) * invd
    v = (dot00 * dot12 - dot01 * dot02) * invd
    return (u >= -eps) and (v >= -eps) and (u + v <= 1.0 + eps)

def _ear_clip_indices(uv, eps=1e-12):
    """
    Triangulate polygon given by UV points (no holes).
    Returns list of index triples.
    """
    n = len(uv)
    if n < 3:
        return []
    if n == 3:
        return [(0, 1, 2)]

    idx = list(range(n))
    tris = []
    ccw = _poly_area2d(uv) > 0.0
    guard = 0
    while len(idx) > 3 and guard < 10000:
        ear_found = False
        m = len(idx)
        for ii in range(m):
            i0 = idx[(ii - 1) % m]
            i1 = idx[ii]
            i2 = idx[(ii + 1) % m]
            a, b, c = uv[i0], uv[i1], uv[i2]

            # skip collinear
            cross = (b.X - a.X)*(c.Y - a.Y) - (b.Y - a.Y)*(c.X - a.X)
            if abs(cross) < eps:
                continue

            if not _is_convex(a, b, c, ccw, eps):
                continue

            # Check no other vertex lies inside the ear
            any_inside = False
            for kk in idx:
                if kk in (i0, i1, i2):
                    continue
                if _pt_in_tri_2d(uv[kk], a, b, c, eps):
                    any_inside = True
                    break
            if any_inside:
                continue

            # Clip ear
            tris.append((i0, i1, i2))
            del idx[ii]
            ear_found = True
            break

        if not ear_found:
            # Fallback: fan from first vertex in the current ring
            for j in range(1, len(idx) - 1):
                tris.append((idx[0], idx[j], idx[j + 1]))
            idx = idx[:3]
        guard += 1

    if len(idx) == 3:
        tris.append((idx[0], idx[1], idx[2]))
    return tris

def _outer_loop_vertices(face, tol):
    """
    Returns (pts3d, uv2d) for the face's OUTER loop, in loop order.
    pts3d: [rg.Point3d, ...]
    uv2d:  [rg.Point2d, ...]   (Face parameter space)
    """
    loop = face.OuterLoop
    if loop is None:
        # Find it explicitly if needed
        for L in face.Loops:
            if L.LoopType == rg.BrepLoopType.Outer:
                loop = L
                break
    if loop is None:
        return [], []

    pts = []
    trims = [t for t in loop.Trims]
    for t in trims:
        e = t.Edge
        if e is None: 
            continue
        # Oriented start vertex of this trim along the loop direction
        v = e.EndVertex if t.IsReversed else e.StartVertex
        p = v.Location
        if not pts or p.DistanceTo(pts[-1]) > tol:
            pts.append(rg.Point3d(p))

    # Remove duplicate closure if present
    if len(pts) > 1 and pts[0].DistanceTo(pts[-1]) <= tol:
        pts.pop()

    # Map to UV for triangulation
    uv = []
    for p in pts:
        ok, u, v = face.ClosestPoint(p)
        if not ok:
            # if this fails, approximate via surface frame projection
            srf = face
            # crude fallback: use world XY as param (won't happen often)
            u, v = p.X, p.Y
        uv.append(rg.Point2d(u, v))

    return pts, uv

# ----------------------------------------------------------------------
# Minimal mesher: preserve tri/quads, triangulate n-gons (>=5)
# ----------------------------------------------------------------------

def minimal_face_mesh(face, out_mesh, tol):
    pts3d, uv = _outer_loop_vertices(face, tol)
    n = len(pts3d)
    if n < 3:
        return

    base = out_mesh.Vertices.Count
    for p in pts3d:
        out_mesh.Vertices.Add(p)  # accepts Point3d

    if n == 3:
        out_mesh.Faces.AddFace(base + 0, base + 1, base + 2)
        return

    if n == 4:
        out_mesh.Faces.AddFace(base + 0, base + 1, base + 2, base + 3)
        return

    # n-gon (>=5): ear-clip in UV using only existing corner vertices
    tri_idx = _ear_clip_indices(uv, eps=tol * 0.1)
    for (i0, i1, i2) in tri_idx:
        out_mesh.Faces.AddFace(base + i0, base + i1, base + i2)

def mesh_brep_preserve_3_4_else_triangulate(brep):
    tol = model_tol()
    out = rg.Mesh()

    # If input is a list, iterate; else wrap
    breps = brep if isinstance(brep, (list, tuple)) else [brep]

    for B in breps:
        if B is None:
            continue
        for face in B.Faces:
            # If face has holes, fallback to Rhino mesher for this face
            has_holes = sum(1 for L in face.Loops if L.LoopType == rg.BrepLoopType.Inner) > 0
            if not has_holes:
                minimal_face_mesh(face, out, tol)
            else:
                # Fallback mesh (may create extra faces but remains valid)
                mp = rg.MeshingParameters()
                mp.SimplePlanes = True
                mp.JaggedSeams = True
                mp.MinimumEdgeLength = 0.0
                mp.MaximumEdgeLength = 1e100  # discourage subdivision
                mparts = rg.Mesh.CreateFromBrep(face.ToBrep(), mp)
                if mparts:
                    for m in mparts:
                        out.Append(m)

    # Cleanup + normals
    out.Faces.CullDegenerateFaces()
    out.Vertices.CullUnused()
    out.Compact()
    try:
        out.UnifyNormals()
    except:
        pass
    out.FaceNormals.ComputeFaceNormals()
    out.Normals.ComputeNormals()
    return out

# ----------------------------------------------------------------------
# Your existing growth/offset step (corrected types & indices)
# ----------------------------------------------------------------------

def subDMesh(M, dist, gen):
    # Ensure normals exist for this generation
    M.FaceNormals.ComputeFaceNormals()
    M.Normals.ComputeNormals()

    out_mesh = rg.Mesh()

    for i in range(M.Faces.Count):
        f = M.Faces[i]

        # Corner indices for tri or quad
        corner_idx = [f.A, f.B, f.C] + ([f.D] if f.IsQuad else [])
        corner_pts = [rg.Point3d(M.Vertices[j]) for j in corner_idx]

        # Face center & normal as doubles
        cf = M.Faces.GetFaceCenter(i)   # Point3f
        nf = M.FaceNormals[i]           # Vector3f
        center = rg.Point3d(cf.X, cf.Y, cf.Z)
        normal = rg.Vector3d(nf.X, nf.Y, nf.Z)

        if normal.IsTiny(1e-12):
            e0 = rg.Vector3d(corner_pts[1] - corner_pts[0])
            e1 = rg.Vector3d(corner_pts[2] - corner_pts[0])
            normal = rg.Vector3d.CrossProduct(e0, e1)

        if not normal.Unitize():
            continue

        center_moved = center + normal * float(dist)

        # Build triangle fan
        fm = rg.Mesh()
        for p in corner_pts:
            fm.Vertices.Add(p)
        c_idx = fm.Vertices.Add(center_moved)

        n_c = len(corner_pts)
        for k in range(n_c):
            k1 = (k + 1) % n_c
            fm.Faces.AddFace(k, k1, c_idx)

        fm.Faces.CullDegenerateFaces()
        fm.Vertices.CullUnused()
        fm.Normals.ComputeNormals()
        fm.Compact()
        out_mesh.Append(fm)

    out_mesh.Faces.CullDegenerateFaces()
    out_mesh.Vertices.CullUnused()
    out_mesh.FaceNormals.ComputeFaceNormals()
    out_mesh.Normals.ComputeNormals()
    out_mesh.Compact()

    if gen > 0:
        return subDMesh(out_mesh, dist / 2.0, gen - 1)
    return out_mesh

# ----------------------------------------------------------------------
# Build the base mesh the way you requested, then run your algorithm
# ----------------------------------------------------------------------

M = mesh_brep_preserve_3_4_else_triangulate(Brep)
a = subDMesh(M, dist, gen)
