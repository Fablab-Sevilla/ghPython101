import Rhino.Geometry as rg

ptList = []

pl1 = []
pl2 = []

for i in range(u+1):
    ptListTemp = []
    for j in range(v+1):
        tempPt = srf.Evaluate(i/u,j/v,2)[1]
        
        ptListTemp.append(tempPt)
    ptList.append(ptListTemp)  

ptList = ptList


for i in range(u):
    for j in range(v):
        
        pt1 = ptList[i][j]
        pt2 = ptList[i+1][j]
        pt3 = ptList[i+1][j+1]
        pt4 = ptList[i][j+1]
        
        pl1.append(rg.Polyline([pt1,pt2,pt4,pt1]))
        pl2.append(rg.Polyline([pt2,pt3,pt4,pt2]))