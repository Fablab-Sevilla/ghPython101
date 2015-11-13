import Rhino.Geometry as rg
from Grasshopper import DataTree as Tree
from Grasshopper.Kernel.Data import GH_Path as Path


ptList = []
polList = []

#Initializing an empty data tree
ptTree = Tree[object]()

for i in range(uDiv+1):
    ptListTemp = []
    
    for j in range(vDiv+1):
        
        ptTemp = srf.Evaluate(i/uDiv,j/vDiv,2)[1]
        ptListTemp.append(ptTemp)
        
    ptList.append(ptListTemp)
    
counter = 0
for i in range(uDiv):
    for j in range(vDiv):
        
        pt0 = ptList[i][j]
        pt1 = ptList[i+1][j]
        pt2 = ptList[i][j+1]
        pt3 = ptList[i+1][j+1]
        
        # Adding points to datatree
        # The commented lines produce the flipped tree.
        #ptTree.Add(pt0,Path(0))
        #ptTree.Add(pt1,Path(1))
        #ptTree.Add(pt2,Path(2))
        #ptTree.Add(pt3,Path(3))
        
        ptTree.AddRange([pt0,pt1,pt3,pt2],Path(counter))
        counter += 1
        
        polList.append(rg.Polyline([pt0,pt1,pt3,pt2]))
        
panel = polList    