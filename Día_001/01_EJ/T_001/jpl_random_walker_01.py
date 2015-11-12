import Rhino.Geometry as rg
import random as r

ptList = []
ptNew = pt0
ptList.append(ptNew)
print ptList
ptPrueba = rg.Point3d(1.0,1.0,0)
print ptPrueba
r.seed(s)

for i in range(it):
    print i
    v3d = rg.Vector3d(r.randint(-1,1),r.randint(-1,1),0)
    ptNew = ptNew + v3d
    
    ptList.append(ptNew)
    
a = ptList

