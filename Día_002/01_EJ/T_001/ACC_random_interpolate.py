import random as rd
import Rhino.Geometry as rg

#Creamos una lista de puntos vacía en la que metemos los puntos que vayamos creando
#Partimos de un punto que elegimos con las coordinadas x e y

ptNew = rg.Point3d(x,y,0)
ptList = []
ptList.append(ptNew)
rd.seed(s)

#bucle
for i in range(It):
    #Se crean coordenadas X e Y que se van incrementando
    coorX = ptNew.X + rd.randint(-1,1)
    coorY = ptNew.Y + rd.randint(-1,1)
    #Se crea un punto en la nueva coordenada
    ptNew = rg.Point3d(coorX, coorY, 0)
    #Se van adjuntando los puntos a la lista
    ptList.append(ptNew)
    
#curva = rg.Curve.CreateControlPointCurve(ptList)
curva = rg.Curve.CreateInterpolatedCurve(ptList,g)
#Probamos con bezier
print curva
#crv = rg.BezierCurve.CreateCubicBeziers(curva,t1,t2)


