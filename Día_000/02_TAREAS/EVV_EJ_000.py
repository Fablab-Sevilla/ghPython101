import rhinoscriptsyntax as rs
import math as m
import ghpythonlib.components as gh

auxPts = []

R=x*C*m.sqrt(It*Alpha)

for i in range(It):
    angTheta = i*Alpha
    #pt = rs.Polar(ptB,angTheta,C*m.sqrt(angTheta))
    xp=C*m.sqrt(angTheta)*m.cos(angTheta)
    yp=C*m.sqrt(angTheta)*m.sin(angTheta)
    zp=m.sqrt(R**2-xp**2-yp**2)-(x-1)*C*m.sqrt(It*Alpha)
    pt = rs.AddPoint(xp,yp,zp)
    auxPts.append(pt)
    
Pts = auxPts 
vor = gh.Voronoi(Pts,rad)
