import rhinoscriptsyntax as rs
import math as m

auxPt = []
for i in range(it):
    angTheta = alpha*i
    radius = C*m.sqrt(angTheta)
    pt = rs.Polar(ptB,angTheta,radius)
    auxPt.append(pt)