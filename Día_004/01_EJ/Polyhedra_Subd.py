import Rhino.Geometry as rg
import ghpythonlib.components as gh

#converting the brep into a simple mesh
M = gh.SimpleMesh(Brep)

centerList = []
newMeshes = []

# We need to compute mesh normals before accessing them
M.Normals.ComputeNormals()



for i in range(M.Faces.Count):
    meshNew = rg.Mesh()
    vertex = M.Faces.GetFaceVertices(i)
    center = M.Faces.GetFaceCenter(i)
    normal = M.FaceNormals.Item[i]
    
    #Unitizing normal vector
    normalU = normal
    normalU.Unitize()
    
    #Moving the face center
    center = center + (normalU.Multiply(normalU,dist))

    for j in range(len(vertex)-1):
        
        meshNew.Vertices.Add(vertex[j+1])
    
    
    meshNew.Vertices.Add(center)
    
    # Caras de 4 lados
    if len(vertex)==5:
    
        meshNew.Faces.AddFace(0,1,4)
        meshNew.Faces.AddFace(1,2,4)
        meshNew.Faces.AddFace(2,3,4)
        meshNew.Faces.AddFace(3,0,4)
    
    # Caras de 3 lados    
    elif len(vertex)==4:
        
        meshNew.Faces.AddFace(0,1,4)
        meshNew.Faces.AddFace(1,2,4)
        meshNew.Faces.AddFace(2,3,4)
    
    meshNew.Normals.ComputeNormals()
    meshNew.Compact()
    
    newMeshes.append(meshNew)
    centerList.append(center)
    
a = newMeshes
    
    
    

    
