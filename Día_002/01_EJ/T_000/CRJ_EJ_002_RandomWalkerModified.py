#CRJ_RandomWalker_Modified

#librerias
import Rhino.Geometry as rg
import math as m
import random as rd
import rhinoscriptsyntax as rs

#semilla
rd.seed(s)

#variable centro poligono
centro=pt0

#bucle
for i in range (It):
    #dibuja un círculo con centro pt0 y radio r
    circle = rg.Circle(centro,r)
    #convertir circulo en curva
    curve = circle.ToNurbsCurve()
    #divide la curva en n partes
    points = rs.DivideCurve(curve,n,False,True)
    #añadir a la lista su primer punto
    points.append(points[0])
    #dibuja lineas
    lines = rs.AddPolyline(points)







