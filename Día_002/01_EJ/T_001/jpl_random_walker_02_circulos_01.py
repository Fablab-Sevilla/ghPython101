﻿import Rhino.Geometry as rg
import random as r

ptlist = []
x = 0
y = 0
z = 0
rad = 0
radlist = [0]
pt0 = rg.Point3d(x,y,z)
ptlist.append(pt0)

for i in range(It):
    x1 = x + r.randint(-1,1)
    y1 = y + r.randint(-1,1)
    pt = rg.Point3d(x1,y1,z)
    #print pt
    ptlist.append(pt)
    rad1 = r.choice([0.6,0.8,1,1.2,1.4])
    radlist.append(rad1)
    x = x1
    y = y1
    #z = z1

a = ptlist
radios = radlist
#print ptlist