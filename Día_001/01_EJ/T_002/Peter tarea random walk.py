import rhinoscriptsyntax as rs
import Rhino as rh
import math as ms
import Grasshopper as gs
#Importamos 3 random (X,Y,Z)
import random as rn
import random as rn1
import random as rn2

#tipos de paso
steps = [-1,0,1]

#Lista de puntos [incluyendo punto inicial] y lineas
pts = [pt0]
lines = []

#Seeds y listas vacias para los valores x,y,z
rn.seed(s)
xlist = []

rn1.seed(s)
ylist = []

rn2.seed(s)

zlist = []

#Descomponemos el punto inicial en x,y,z
pt = rs.PointCoordinates(pt0)

ptx = pt[0]
pty = pt[1]
ptz = pt[2]

#comenzamos a calcular los pasos en cada dimension
for i in range(It):
    #Pasos en cada dirección 
    x = rn.choice(steps)
    y = rn1.choice(steps)
    #CONTROL DIMENSIONAL
    if dim==0:
         z = rn2.choice(steps)
    else:
        z=0
    #FIN DEL CONTROL DIMENSIONAL-->creemos listas!
    
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)
    
    stepx = xlist[i]
    stepy = ylist[i]
    stepz = zlist[i]
    
    #Sumatorios de pasos y construcción de los puntos (punto inicial más el sumatorio de pasos)
    x = sum(xlist)
    y = sum(ylist)
    z = sum(zlist)
    
    
    pt = rs.AddPoint((ptx+x),(pty+y),(ptz+z))
    #Todos los puntos a una lista y hacemos polyline
    pts.append(pt)
ptList = pts
lines = rs.AddPolyline(ptList)
