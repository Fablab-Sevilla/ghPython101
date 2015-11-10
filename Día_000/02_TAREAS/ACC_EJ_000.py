import rhinoscriptsyntax as rs
import math as m
import ghpythonlib.components as gh

auxPts = []
for i in range(It):
    angTheta = i*Alpha
    angFi = i*Betha
    x = C*m.sqrt(angTheta)*m.sqrt(angFi)*m.sin(angTheta)*m.cos(angFi)
    y = C*m.sqrt(angTheta)*m.sqrt(angFi)*m.sin(angTheta)*m.sin(angFi)
    z = C*m.sqrt(angTheta)*m.sqrt(angFi)*m.cos(angTheta)
    pt = rs.AddPoint(x,y,z)
    auxPts.append(pt)

Pts = auxPts 
#dela = gh.Delaunay(Pts)
