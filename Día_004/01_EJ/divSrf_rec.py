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

def divSrf(uD,vD,srf):
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
            
            # Transforming [0,1] domain coortinates to Surface
            # domain
            cU = lerp(srf.Domain(0)[0],srf.Domain(0)[1],i/uD)
            cV = lerp(srf.Domain(1)[0],srf.Domain(1)[1],j/vD)
        
            ptTemp = srf.Evaluate(cU,cV,2)[1]
            ptListTemp.append(ptTemp)
            uvPtTemp.append(ptUV)
        
        ptList.append(ptListTemp)
        uvPtList.append(uvPtTemp)
        
   
#     pan = createPanel(ptList, T)
#      
#     # limitando iteraciones
#     for d in pan[1]:
#            
#         if d > T:
#                
#             a = 1
        
    return [ptList,uvPtList]

def createPanel(pts,T):
    
    polList = []
    devList = []
    counter = 0
    
    for i in len(pts)-1:
        for j in len(pts[i]-1):
            
            pt0 = ptList[i][j]
            pt1 = ptList[i+1][j]
            pt2 = ptList[i][j+1]
            pt3 = ptList[i+1][j+1]
            
            plane = rg.Plane(pt0,pt1,pt2)
            newPt3 = plane.ClosestPoint(pt3)
            dev = pt3.DistanceTo(newPt3)
            pt3 = newPt3
            
            polList.append(rg.Polyline([pt0,pt1,pt3,pt2,pt0]))
            devList.append(dev)
            pass
    
    return [polList,devList]
    pass


panels = divSrf(uDiv,vDiv,srf)
ptList = panels[0]
uvPtList = panels[1]


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
        pt3 = newPt3
        
        
        
        
        #ptTree.AddRange([pt0,pt1,pt3,pt2],Path(counter))
        #counter += 1
        polList.append(rg.Polyline([pt0,pt1,pt3,pt2,pt0]))
    
    
        
panel = polList    