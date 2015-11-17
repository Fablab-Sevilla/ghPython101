import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import random as rd

def addPolygon(p,n):
    #inicializamos pts para diferenciarla de pts global
    pts = []
    for i in range(n):
        pts.append(rs.Polar(p,i*step,r))
        
    ptM = (pts[0]+pts[1])/2       
    dist = rs.Distance(ptM,p)
    
    pts.append(pts[0]) # Appends the first point again to close the curve
    pol = rg.PolylineCurve(pts) 
    return [pol,dist]

rd.seed(s)
pts = []
pol = []
step = 360.0/n

# Creates a loop to build points with polar coordinates
# at 2Pi/n increments.

angleList = [((step)*i)+step/2 for i in range(n)]
pts.append(pt)
pol.append(addPolygon(pt,n)[0])
ptNew = pt

for i in range(it):
    
    rdAngle = rd.choice(angleList)
    polygon = addPolygon(ptNew,n)
   
    pol.append(polygon[0])
    #print pol
    
    ptNew = rs.Polar(ptNew,rdAngle,polygon[1]*2)
    pts.append(ptNew)
    
print pol
pol = rg.Brep.CreatePlanarBreps(pol)