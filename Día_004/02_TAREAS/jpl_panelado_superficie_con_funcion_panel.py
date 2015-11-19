import Rhino.Geometry as rg

def panelGen(pt0,pt1,pt2,pt3):
    pan = rg.PolylineCurve([pt0,pt1,pt2,pt3,pt0])

    return pan
    
#print panel

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
        
        pt0a = ptList[i][j]
        pt1a = ptList[i+1][j]
        pt2a = ptList[i+1][j+1]
        pt3a = ptList[i][j+1]
        
        panel = panelGen(pt0a,pt1a,pt2a,pt3a)
        
        polList.append(panel)
        
panels = polList