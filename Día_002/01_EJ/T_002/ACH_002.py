import rhinoscriptsyntax as rs
import random as rd
import Rhino.Geometry as rg

Ptnew = Pt0
PtList = [Pt0]
rd.seed(S)
#DistList = []
LineasList = []
Medios = []
Circulos = []
for i in range(It):
    
    Angle = rd.randint(Amin,Amax)
    R = rd.randint(Rmin,Rmax)
    
    Ptnew = rs.Polar(Ptnew, Angle, R)
    
    PtList.append(Ptnew)
    
    dist = rs.Distance(Ptnew, PtList[-2])/2
    print dist
    if dist == 0:
        dist = 0.01
    else:
        dist = dist       
    Lineas=rs.AddLine(Ptnew,PtList[-2])
    
    LineasList.append(Lineas)
    
    PtMedio = rs.CurveMidPoint(Lineas)
    Medios.append(PtMedio)
    
    Circle = rs.AddCircle(PtMedio,dist)
    Circulos.append(Circle)
    
    