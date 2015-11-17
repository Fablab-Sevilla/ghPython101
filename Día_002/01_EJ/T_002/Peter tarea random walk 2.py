import rhinoscriptsyntax as rs
#Importamos random 
import random as rn
#Creamos seed y listas para los puntos, lineas y triangulos
rn.seed(s)
pts = [pt0]
lines = []
triangles = []
newptList = [pt0]
#Iteramos para la creacion de cada punto linea y triangulo
for i in range(It):
    #los puntos en polares con angulos y pasos controladp
    angulos = rn.randint(Amin,AMAX)
    steps = rn.randint(Rmin,RMAX)
    NewPts = rs.Polar((pts[-1]),angulos,steps)
    pts.append(NewPts)
    
    #Una vez creado los puntos creamos los triangulos,
    #Primero la linea y el punto medio
    a = pts[i] 
    b = pts[i+1]
    line = rs.AddLine(a,b)
    lines.append(line)
    mid = rs.CurveMidPoint(line)
    
    #Sacamos el vector normal a la recta y lo escalamos por un random
    rnleng = ((rn.randint(3,10))/10)
    z = rs.CurveNormal(line)
    vector = rs.VectorCreate(a,b)
    nor = rs.VectorCrossProduct(vector,z)
    normal = rs.VectorScale(nor,rnleng)
    trans1 = rs.XformTranslation(normal)
    trans2 = rs.XformTranslation(rs.VectorReverse(normal))
    
    
    #Desplazamos los puntos medios el vector normal escalado
    newpts1 = rs.PointTransform(mid,trans1)
    newpts2 = rs.PointTransform(mid,trans2)
    
    #Creamos el triangulo con polyline
    if rs.Distance(newpts1,newptList[-1])>rs.Distance(newpts2,newptList[-1]):
        newpts = newpts1
    else:
        newpts = newpts2
    
    tri = rs.AddPolyline([a,b,newpts,a])
    triangles.append(tri)
    
ptList = pts

