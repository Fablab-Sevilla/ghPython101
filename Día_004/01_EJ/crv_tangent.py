import Rhino.Geometry as rg
import random as rd

rd.seed(n)
counter = 0

def findTangent(c,pt):
    
    areaCrv = rg.AreaMassProperties.Compute(c)
    centroid = areaCrv.Centroid
    #rGuess = rd.uniform(crv.Domain[0],crv.Domain[1])
    ptGuess = crv.PointAt(0)
    distRef = pt.DistanceTo(centroid)
    
    #ray = rg.Ray3d(p,rg.Vector3d(crv.PointAt(rGuess),pt)
    ray = rg.Line(pt,ptGuess-pt,distRef*100)
    ray = rg.LineCurve(ray)
    
    # Calculating the intersection
    interRay = rg.Intersect.Intersection.CurveCurve(ray, c, 0.0001, 0.0001)
    
    # Extracting parameters to splic curve
    paramList = [i.ParameterB for i in interRay]
    
    crvList = c.Split(paramList)
    
    while len(interRay)>1 :
        
        if len(interRay) == 0:
            
            ray.Rotate(-0.01, rg.Vector3d.ZAxis, pt)
        else:
            ray.Rotate(0.01, rg.Vector3d.ZAxis, pt)    
            
        interRay = rg.Intersect.Intersection.CurveCurve(ray, c, 0.0001, 0.0001)
        
    
            
    print interRay
    print len(interRay)    
    # Dealing with one-point/two-point intersections.
    if len(interRay)>1:
     
        return [interRay[0].PointA, interRay[1].PointA,crvList]
     
    else:
         
        return[interRay[0].PointA,crvList]



tangent = findTangent(crv, p)

print tangent
#a = tangent[:len(tangent)-1]
#b = tangent[len(tangent)-1]

#a = parts