import rhinoscriptsyntax as rs
import math as m

ptList = []

def koch(ptA, ptB, r0, r1, r2, rM):
    
    #points = []
    
    pt0 = ((ptB-ptA)*r0)+ptA
    pt1 = ((ptB-ptA)*r1)+ptA
    
    #Calculating vector perpendicular to ptB-ptA
    cross = rs.VectorCrossProduct((ptB-ptA),(0,0,1))
    cross = rs.VectorUnitize(cross)
    dist = rs.VectorLength((ptB-ptA))
    h = m.sqrt(((dist/3)**2.0)-((dist/6)**2.0))
    pt1 += cross*(h*rM)
    
    pt2 = ((ptB-ptA)*r2)+ptA
    
    #points.extend((pt0,pt1,pt2))
    return [ptA,pt0,pt1,pt2,ptB]
    
def recursive (ptA, ptB, gens, list):
    if gens>0:
        
        newPts = koch (ptA,ptB,rat0,rat1,rat2,ratM)
        curve = rs.AddPolyline(newPts)
        
        if gens == 1:
            list.append(curve)
        
        recursive(newPts[0],newPts[1],gens-1,list)
        recursive(newPts[1],newPts[2],gens-1,list)
        recursive(newPts[2],newPts[3],gens-1,list)
        recursive(newPts[3],newPts[4],gens-1,list)
       
        gens-=1 
        return list
        
crv = recursive(PtA,PtB,G,ptList)  