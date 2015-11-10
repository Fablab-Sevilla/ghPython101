"""" =====================================
Mini-project # 002
Random Walker
v.1(10/11/2015)
Enrique Vazquez
=========================================

Traza una ruta aleatoria partiendo de un punto

"""

# Carga de librerias --------------------
import math as m
import random as rd
import Rhino.Geometry as rg
#import ghpythonlib.components as gh
#import rhinoscriptsyntax as rs


# Variables iniciales --------------------
ruta=[] # lineas de la ruta
listPt=[] # lista de puntos de la ruta
newPt=Pto # variable para el bucle
listPt.append(newPt) # añade a la lista el punto inicial


# Semilla --------------------------------
rd.seed(s)


""" Cuerpo de la rutina.
Generación de los puntos y lineas de la ruta
------------------------------------------"""
for i in range(1,It):
    m=rd.randint(-1,1)
    n=rd.randint(-1,1)
    movmt=rg.Vector3d(m,n,0) # vector desplazamiento
    """ el nuevo punto se calcula mediante un desplzamiento a
    partir del punto anterior"""
    newPt=newPt+movmt
    listPt.append(newPt) #se añade el nuevo punto a la lista
    ruta.append(rg.Line(listPt[i-1],listPt[i])) #se alñade la nueva ruta a la lista