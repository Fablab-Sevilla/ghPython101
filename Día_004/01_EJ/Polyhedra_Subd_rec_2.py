import Rhino.Geometry as rg
import ghpythonlib.components as gh

# Convert Brep to a mesh
M = gh.SimpleMesh(Brep)

def subDMesh(M, dist, gen):
    # Make sure normals exist for this generation
    M.FaceNormals.ComputeFaceNormals()
    M.Normals.ComputeNormals()

    out_mesh = rg.Mesh()

    for i in range(M.Faces.Count):
        face = M.Faces[i]

        # Unique corner indices
        corner_idx = [face.A, face.B, face.C] + ([face.D] if face.IsQuad else [])
        corner_pts = [M.Vertices[j] for j in corner_idx]  # Point3f

        # ---- type-safe center & normal math (Fix A)
        center_f = M.Faces.GetFaceCenter(i)   # Point3f
        n_f = M.FaceNormals[i]                # Vector3f

        center = rg.Point3d(center_f.X, center_f.Y, center_f.Z)
        n = rg.Vector3d(n_f.X, n_f.Y, n_f.Z)

        if n.Length < 1e-12:
            e0 = rg.Vector3d(corner_pts[1] - corner_pts[0])
            e1 = rg.Vector3d(corner_pts[2] - corner_pts[0])
            n = rg.Vector3d.CrossProduct(e0, e1)

        if not n.Unitize():
            # Skip pathological faces with zero-length normal
            continue

        center_moved_3d = center + n * float(dist)
        center_moved = rg.Point3f(center_moved_3d.X, center_moved_3d.Y, center_moved_3d.Z)
        # ----

        # Local mesh for this face
        fm = rg.Mesh()
        for p in corner_pts:
            fm.Vertices.Add(p)
        c_idx = fm.Vertices.Add(center_moved)

        # Triangle fan (wrap with modulo)
        n_corners = len(corner_pts)
        for k in range(n_corners):
            k1 = (k + 1) % n_corners
            fm.Faces.AddFace(k, k1, c_idx)

        # Clean up the local mesh
        fm.Faces.CullDegenerateFaces()
        fm.Vertices.CullUnused()
        fm.Normals.ComputeNormals()
        fm.Compact()

        out_mesh.Append(fm)

    # Prepare the output mesh for recursion
    out_mesh.Faces.CullDegenerateFaces()
    out_mesh.Vertices.CullUnused()
    out_mesh.FaceNormals.ComputeFaceNormals()
    out_mesh.Normals.ComputeNormals()
    out_mesh.Compact()

    if gen > 0:
        return subDMesh(out_mesh, dist / 2.0, gen - 1)
    else:
        return out_mesh

a = subDMesh(M, dist, gen)
