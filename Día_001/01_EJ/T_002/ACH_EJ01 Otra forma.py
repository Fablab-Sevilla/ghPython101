#Importamos los modulos
import random as rd
import Rhino.Geometry as rg

"""Establecemos las relaciones y creamos la lista vacía a la que 
adjuntaremos los puntos que vayamos creando
Se le da un valor seed al componente aleatorio para que los
resultados sean controlados dentro de la aleatoriedad"""

Ptnew = PtB
PtList = []
rd.seed(5)

#Creamos el bucle

for i in range(It):
    #Se generan variables con valores aleatorios enteros entre -1 y 1

    aleatorioX = rd.randint(-1,1)
    aleatorioY = rd.randint(-1,1)

    """Se crean coordenadas X e Y que se van incrementando con los valores de 
    esas variables y que van usando el punto que se genera en el bucle anterior"""

    Pt1X = Ptnew.X + (aleatorioX)
    Pt1Y = Ptnew.Y + (aleatorioY)

#Se crea el Punto en la coordenada

    Ptnew = rg.Point3d(Pt1X,Pt1Y,0)

#Se va adjuntando el punto a la lista Plist por cada bucle

    PtList.append(Ptnew)

#Se crea la polilinea

LinePt = rg.PolylineCurve(PtList)