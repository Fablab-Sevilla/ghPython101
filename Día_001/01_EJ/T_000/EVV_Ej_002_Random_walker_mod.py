# =====================================
# Mini-project # 002
# Random Walker
# v.2.0(12/11/2015)
# Enrique Vazquez
# =========================================

# Traza una ruta aleatoria partiendo de un punto


# Carga de librerias --------------------
import math as m
import random as rd
import Rhino.Geometry as rg
#import ghpythonlib.components as gh
import rhinoscriptsyntax as rs


# Variables iniciales --------------------
#ruta=[] # lineas de la ruta
listCt=[] # lista de puntos de la ruta
center=Pto # variable para el bucle
listCt.append(center) # añade a la lista el punto inicial
listPtos=[]



# Semilla --------------------------------
rd.seed(s)


# Cuerpo de la rutina.
# Generación de los puntos y lineas de la ruta
# ------------------------------------------
for i in range(0,It):
    circle=rg.Circle(center,r)
    curve=rg.Circle.ToNurbsCurve(circle)
    ptos=rs.DivideCurve(curve,n)
    ptos.append(ptos[0])
    polig=rs.AddPolyline(ptos)
    lines=rs.ExplodeCurves (polig, True)
    #nlin
    #simetr=
    
    
    #m=2*rd.randint(-1,1)
    #n=2*rd.randint(-1,1)
    #movmt=rg.Vector3d(m,n,0) # vector desplazamiento
    # el nuevo punto se calcula mediante un desplzamiento a
    # del punto anterior
    #newPt=newPt+movmt
    #listPt.append(newPt) #se añade el nuevo punto a la lista
    #ruta.append(rg.Line(listPt[i-1],listPt[i])) #se alñade la nueva ruta a la lista



#ruta(rg.BezierCurve(controlPoints: listPt)