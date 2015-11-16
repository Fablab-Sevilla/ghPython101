import Rhino.Geometry as rg
import Rhino.Display as rdis
import random as rd
import math as m

ptList = []
colList = []

rd.seed(s)

for i in range(50):
    for j in range(50):
        
        z = rd.gauss(me,dev)
        ptList.append(rg.Point3d(i,j,z))
        col = rdis.ColorHSL(z*0.2,1,0.5)
        colList.append(col.ToArgbColor())
        
a = ptList       