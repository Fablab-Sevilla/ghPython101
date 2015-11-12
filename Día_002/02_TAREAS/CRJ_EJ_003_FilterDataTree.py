#CRJ_EJ003_Filter DataTree

#librerias
import Rhino.Geometry as rg

#lista
ptList = []
polList = []

#bucle doble para generar los puntos. Toma el primer elemento del primer bucle y lo combina con todos los del segundo
for i in range (uDiv+1):
    ptListTemp = []

    for j in range (vDiv+1):
        ptTemp = srf.Evaluate(i/uDiv,j/vDiv,2) [1]
        ptListTemp.append (ptTemp)
        
#lista que contiene sublistas de puntos (columnas de la matriz)
    ptList.append(ptListTemp)
    #para acceder a valores de una lista dentro de otra lista
    #tomar la primera sublista
    #ptList [0]
    #tomar el segundo valor de la primera sublista
    #ptList [0][1]
    


#nuevo bucle doble para generar los paneles.
#separar todos los primeros puntos de los paneles en una lista, todos los segundos en otra...hacer 4 listas
for i in range (uDiv):
    for j in range (vDiv):
        pt0 = ptList [i][j]
        pt1 = ptList [i+1][j]
        pt2 = ptList [i][j+1]
        pt3 = ptList [i+1][j+1]
        
        #Unimos los puntos con una polilinea
        polList.append(rg.Polyline([pt0,pt1,pt3,pt2,pt0]))
        
panel = polList




