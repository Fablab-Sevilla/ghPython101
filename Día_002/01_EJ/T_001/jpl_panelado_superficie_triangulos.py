#panelado triangulos
import Rhino.Geometry as rg

ptList = []
polList = []

for i in range(uDiv+1):
    ptListTemp = []
    for j in range(vDiv+1):
        
        #print "puntos " + str(i) + "." + str(j)
        #atencion superficie reparametrizada en gh
        ptTemp = srf.Evaluate(i/uDiv,j/vDiv,2)[1]
        ptListTemp.append(ptTemp)
        
    ptList.append(ptListTemp)
    #print ptList

for i in range(uDiv):
    for j in range(vDiv):
        pt0 = ptList[i][j]
        pt1 = ptList[i+1][j]
        pt2 = ptList[i+1] [j+1]
        pt3 = ptList[i][j+1]
        
        polList.append(rg.Polyline([pt0,pt1,pt3,pt0]))
        polList.append(rg.Polyline([pt1,pt2,pt3,pt1]))
        
panel = polList