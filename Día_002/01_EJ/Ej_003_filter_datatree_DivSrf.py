import Rhino.Geometry as rg
from Grasshopper import DataTree as Tree
from Grasshopper.Kernel.Data import GH_Path as Path

ptList = []
ptTree = Tree[object]()
pl = []

for i in range(uDiv+1):
    ptListTemp = []
    for j in range(vDiv+1):
        
        tempPt = srf.Evaluate(i/uDiv,j/vDiv,2)[1]
        ptTree.Add(tempPt,Path(i))
        ptListTemp.append(tempPt)
    ptList.append(ptListTemp)       

for i in range(uDiv):
    for j in range(vDiv):
        
        pt1 = ptList[i][j]
        pt2 = ptList[i+1][j]
        pt3 = ptList[i][j+1]
        pt4 = ptList[i+1][j+1]
        
        pl.append(rg.Polyline([pt1,pt2,pt4,pt3,pt1]))
        
