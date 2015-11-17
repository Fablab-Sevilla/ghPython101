import Rhino.Geometry as rg
import random as r

ptList = []
ptNew = pt0
r.seed(s)

for i in range(it):
    
    # Avoiding error produced by pt0 being outside the curve
    if rg.BrepTrim.Contains(crv,pt0) == rg.PointContainment.Outside: break
    
    # Keep a record of the last point created
    if i == 0:
        
        lastPt = pt0 # In this iteration len(ptList) == 0
    else:
        lastPt = ptList[-1]    
     
    # Calculating the new vector and point    
    newv3d = rg.Vector3d(r.randint(-1,1),r.randint(-1,1),0)
    ptNew = lastPt + newv3d       
    
    # If the new point is not inside the curve, calculate the vector to go back in.
    while rg.BrepTrim.Contains(crv,ptNew) == rg.PointContainment.Outside:
        newv3d = rg.Vector3d(r.randint(-1,1),r.randint(-1,1),0)
        ptNew = lastPt + newv3d
  
    ptList.append(ptNew)
    
a = ptList