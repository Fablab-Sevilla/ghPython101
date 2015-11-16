'''
Ejercicio 03. v02

CONTROL DE CAMBIOS

Depurado del código y ordenar los elementos por grupos.

'''

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

ptList = []
ptListP = []
pl = []
triP = []

#Obtenemos puntos de la superficie en una lista de lista. Matriz
for i in range(uDiv+1):
    ptListTemp = []
    for j in range(vDiv+1):
        
        ptTemp = srf.Evaluate(i/uDiv,j/vDiv,2)[1]
        ptListTemp.append(ptTemp)
    ptList.append(ptListTemp)

#dibujar polilinea de 4 lados no coplanarios.
for i in range(uDiv):
    for j in range(vDiv):
        #puntos para cada subdivision que recorre la superficie
        pt1 = ptList[i][j]
        pt2 = ptList[i+1][j]
        pt3 = ptList[i+1][j+1]
        pt4 = ptList[i][j+1]
        
        #Añadimos polilineas a una lista para sacar el resultado
        pl.append(rg.Polyline([pt1,pt2,pt3,pt4,pt1]))
        
        #Generamos para cada triangulo una lista de tres puntos
        trianguloA = []
        trianguloB = []
        trianguloA.append(pt1)
        trianguloA.append(pt2)
        trianguloA.append(pt4)
        trianguloB.append(pt2)
        trianguloB.append(pt4)
        trianguloB.append(pt3)
        
        #creo las superficies que barren la superficie
        triP.append(rs.AddSrfPt(trianguloA))
        triP.append(rs.AddSrfPt(trianguloB))