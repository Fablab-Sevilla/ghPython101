import Rhino.Geometry as rg
import random as rd

rd.seed(n)

def findTangent(c,pt):
    
    areaCrv = rg.AreaMassProperties.Compute(c)
    centroid = areaCrv.Centroid
    rGuess = rd.uniform(crv.Domain[0],crv.Domain[1])
    ptGuess = crv.PointAt(rGuess)
    distRef = pt.DistanceTo(centroid)
    
    #ray = rg.Ray3d(p,rg.Vector3d(crv.PointAt(rGuess),pt)
    ray = rg.Line(pt,ptGuess-pt,distRef*100)
    ray = rg.LineCurve(ray)
    
    # Calculating the intersection
    interRay = rg.Intersect.Intersection.CurveCurve(ray, c, 0.0001, 0.0001)
    
    # Extracting parameters to splic curve
    paramList = [i.ParameterB for i in interRay]
    print paramList
    
    c.ChangeClosedCurveSeam(paramList[0])
    crvList = c.Split(paramList)
    
    print crvList
    
    # Dealing with one-point/two-point intersections.
    if len(interRay)>1:
    
        return [interRay[0].PointA, interRay[1].PointA,crvList]
    
    else:
        
        return[interRay[0].PointA,crvList]



tangent = findTangent(crv, p)
a = tangent[:len(tangent)-1]
b = tangent[len(tangent)-1]

#a = parts