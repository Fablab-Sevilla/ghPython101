import rhinoscriptsyntax as rs
import math as m
import ghpythonlib.components as gh

auxPts = []

for i in range(It):
    angTheta = i*Alpha
    pt = rs.Polar(ptB,angTheta,C*m.sqrt(angTheta))
    auxPts.append(pt)
    
Pts = auxPts 
vor = gh.Voronoi(Pts,rad)