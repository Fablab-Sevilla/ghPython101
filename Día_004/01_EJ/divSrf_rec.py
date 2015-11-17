import Rhino.Geometry as rg
from Grasshopper import DataTree as Tree
from Grasshopper.Kernel.Data import GH_Path as Path


ptList = []
polList = []
uvPtList = []

#Initializing an empty data tree
ptTree = Tree[object]()

def lerp(a,b,x):
    
    '''
    Returns a value y that is the linear interpolation
    between a and b (being a and b positive numbers)
    at x position related to a [0,1] base domain.
    '''
    
    return ((b-a)*x)+a

def panelize(uD,vD,srf):
    '''
    Creates panels in a surface given the number of
    divisions in u and v direction, using T as tolerance
    for subdivision purposes.
    '''
    
    # Initializing lists
    ptList = []
    uvPtList = []
    
    for i in range(uD+1):
        ptListTemp = []
        uvPtTemp = []
        for j in range(vD+1):
        
            # Storing point UV coordinates
            parU = i/uD
            parV = j/vD
            ptUV = rg.Point2d(parU,parV)
            
            cU = lerp(srf.Domain(0)[0],srf.Domain(0)[1],i/uD)
            cV = lerp(srf.Domain(1)[0],srf.Domain(1)[1],j/vD)
        
            ptTemp = srf.Evaluate(cU,cV,2)[1]
            ptListTemp.append(ptTemp)
            uvPtTemp.append(ptUV)
        
        ptList.append(ptListTemp)
        uvPtList.append(uvPtTemp)
        
    return [ptList,uvPtList]


panels = panelize(uDiv,vDiv,srf)
ptList = panels[0]


counter = 0
for i in range(uDiv):
    for j in range(vDiv):
    
        pt0 = ptList[i][j]
        pt1 = ptList[i+1][j]
        pt2 = ptList[i][j+1]
        pt3 = ptList[i+1][j+1]
    
        
        plane = rg.Plane(pt0,pt1,pt2)
        newPt3 = plane.ClosestPoint(pt3)
        dev = pt3.DistanceTo(newPt3)
        
            
        
        #ptTree.AddRange([pt0,pt1,pt3,pt2],Path(counter))
        #counter += 1
        polList.append(rg.Polyline([pt0,pt1,pt3,pt2,pt0]))
    
    
        
panel = polList    