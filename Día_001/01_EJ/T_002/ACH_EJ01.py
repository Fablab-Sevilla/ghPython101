import rhinoscriptsyntax as rs
import random as rd
import Rhino.Geometry as rg

Ptnew = Pt0
PtList = []
rd.seed(s)

for i in range(It):
    
    SumaX = rd.randint(-1,1)
    
    SumaY = rd.randint(-1,1)
    
    Ptnew = rg.Point3d(Ptnew.X + SumaX, Ptnew.Y + SumaY,0)
    
    PtList.append(Ptnew)
    
    Linea = rg.PolylineCurve(PtList)

