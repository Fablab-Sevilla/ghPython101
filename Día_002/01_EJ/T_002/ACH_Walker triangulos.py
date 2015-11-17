import rhinoscriptsyntax as rs
import random as rd

ptNew = Pt0
ptList = [Pt0]
rd.seed(S)
linesList = []
mid = []
alturasList = []
triangulos = []

for i in range(It):
    Angle = rd.randint(Amin,Amax)
    R = rd.randint(Rmin,Rmax)
    
    ptNew = rs.Polar(ptNew, Angle, R)
    ptList.append(ptNew)
    dist = rs.Distance(ptNew, ptList[-2])/2   
    #Se crean las lineas
    lines = rs.AddLine(ptNew,ptList[-2])    
    linesList.append(lines)
    #Se crean los puntos medios de las mismas
    midPt = rs.CurveMidPoint(lines)
    mid.append(midPt)
    
    long = rd.randint(1,5)/10
    normalz = rs.CurveNormal(lines)
    vector = rs.VectorCreate(ptNew, ptList[-2])
    altura = rs.VectorCrossProduct(normalz,vector)
    vScal = rs.VectorScale(altura, long)
    transformacion = rs.XformTranslation(vScal)
    
    ptAltura = rs.PointTransform(midPt, transformacion)
    alturasList.append(ptAltura)
    
    triangulo = rs.AddPolyline([ptNew, ptAltura, ptList[-2]])
    
    triangulos.append(triangulo)