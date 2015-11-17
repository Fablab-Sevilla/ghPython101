import Rhino.Geometry as rg

ptList = []
polList = []
polList1 = []

for i in range (uDiv+1):
    ptListTemp = []
    for j in range(vDiv+1):
        
        ptTemp = srf.Evaluate(i/uDiv,j/vDiv,2)[1]
        ptListTemp.append(ptTemp)
        #print ptTemp
        #print "Punto " + str(i) + "_" + str(j) 
    ptList.append(ptListTemp)     
    
for i in range (uDiv):
    for j in range (vDiv):
        pt0 = ptList[i][j]
        pt1 = ptList[i+1][j]
        pt2 = ptList[i+1][j+1]
        pt3 = ptList[i][j+1]
        
        polList.append(rg.Polyline([pt0,pt1,pt3,pt0]))
        polList1.append(rg.Polyline([pt1,pt2,pt3,pt1]))
        
    panel1 = polList
    panel2 = polList1
    