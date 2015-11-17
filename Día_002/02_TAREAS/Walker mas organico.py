import rhinoscriptsyntax as rs
import random as rd
import Rhino.Geometry as rg

ptNew = Pt0
ptList = [Pt0]
rd.seed(S)
linesList = []
mid = []
Circles = []
#Se genera el bucle que ira creando los puntos
for i in range(It):
    #Los puntos se crean por coordenadas polares y valores aleatorios
    #de angulo y radio
    Angle = rd.randint(Amin,Amax)
    R = rd.randint(Rmin,Rmax)
    
    ptNew = rs.Polar(ptNew, Angle, R)
    
    ptList.append(ptNew)
    #Como primero adjunto el nuevo punto a la lista, se debe colocar
    #el valor [-2]
    dist = rs.Distance(ptNew, ptList[-2])/2
    #evito el error de la distancia 0 que luego sera el radio de
    #las circunferencias
    if dist == 0:
        dist = 0.01
    else:
        dist = dist    
    #Se crean las lineas
    lines = rs.AddLine(ptNew,ptList[-2])
    
    linesList.append(lines)
    #Se crean los puntos medios de las mismas
    midPt = rs.CurveMidPoint(lines)
    mid.append(midPt)
    #Se crean las circunferencias y se transforman a NURBS para operar con ellas    
    Circle = rg.Circle(midPt,dist)
    Circle = Circle.ToNurbsCurve()
    
    Circles.append(Circle)
    
    #Se crean los breps desde los circulos, se fusionan y se extrae
    #la curva del perimetro
    brep = rg.Brep.CreatePlanarBreps(Circles)
    merge = rg.Brep.MergeBreps(brep,5)
    edges = rg.Brep.DuplicateNakedEdgeCurves(merge,True,False)