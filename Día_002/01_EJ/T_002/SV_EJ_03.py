import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

ptList = []
ptListP = []
pl = []
triP = []

#Obtenemos puntos de la superficie en una lista de lista
for i in range(uDiv+1):
    ptListTemp = []
    for j in range(vDiv+1):
        
        ptTemp = srf.Evaluate(i/uDiv,j/vDiv,2)[1]
        ptListTemp.append(ptTemp)
    ptList.append(ptListTemp)

#dibujar polilinea de 4 lados no coplanarios.
for i in range(uDiv):
    for j in range(vDiv):
        #puntos
        pt1 = ptList[i][j]
        pt2 = ptList[i+1][j]
        pt3 = ptList[i+1][j+1]
        pt4 = ptList[i][j+1]
        #Añadimos polilinea a una lista para sacar el resultado
        pl.append(rg.Polyline([pt1,pt2,pt3,pt4,pt1]))

#superficie triangulando A-B
for i in range(uDiv):
    for j in range(vDiv):
        
        #Triangulando malla A
        trianguloA = []
        pt5 = ptList[i][j]
        pt6 = ptList[i+1][j]
        pt7 = ptList[i][j+1]
        trianguloA.append(pt5)
        trianguloA.append(pt6)
        trianguloA.append(pt7)
        triP.append(rs.AddSrfPt(trianguloA))
        
        #Triangulando malla B
        trianguloB = []
        pt8 = ptList[i+1][j+1]
        trianguloB.append(pt6)
        trianguloB.append(pt7)
        trianguloB.append(pt8)
        triP.append(rs.AddSrfPt(trianguloB))