import Rhino.Geometry as rg
import random as r

ptlist = []
x = 0
y = 0
z = 0
pt0 = rg.Point3d(x,y,z)
ptlist.append(pt0)

for i in range(It):
    x1 = x + r.randint(-1,1)
    y1 = y + r.randint(-1,1)
    #z1 = z + r.randint(-2,3)
    z1 = 0
    pt = rg.Point3d(x1,y1,z1)
    #print pt
    ptlist.append(pt)
    x = x1
    y = y1
    #z = z1

a = ptlist
#print ptlist