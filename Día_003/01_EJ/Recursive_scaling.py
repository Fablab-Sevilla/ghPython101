import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math as m


def scaling(c):
    
    crvArea = rs.CurveArea(c)[0]
    crvCentroid = rs.CurveAreaCentroid(c)[0]
    #print crvCentroid
    
    # Comprobando casos
    if abs(target-crvArea)>tolerance:
        if target > crvArea:
            print "caso_0"
            print "Targe-Area= %f" %abs(target-crvArea)
            print "Tolerance= %f" %tolerance
            print "////////////////////////////////////////////"
        
            crvNew = rs.ScaleObject(c,crvCentroid,[1+step,1+step,0])
            c = scaling(crvNew)
        
        elif target < crvArea:
            print "caso_1"
            print "Targe-Area= %f" %(target-crvArea)
            print "Tolerance= %f" %tolerance
            print "////////////////////////////////////////////"
        
            crvNew = rs.ScaleObject(c,crvCentroid,[1-step,1-step,1-step])
            c = scaling(crvNew)
    
    #print "out"
    return c
        
        
a = scaling(crv)
print a