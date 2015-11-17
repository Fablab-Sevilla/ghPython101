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
    
    #Sacamos el vector normal a la recta y lo escalamos por un random
    rnleng = ((rn.randint(3,5))/10)
    z = rs.CurveNormal(line)
    vector = rs.VectorCreate(a,b)
    nor = rs.VectorCrossProduct(vector,z)
    normal = rs.VectorScale(nor,rnleng)
    trans1 = rs.XformTranslation(normal)
    trans2 = rs.XformTranslation(rs.VectorReverse(normal))
    
    
    #Desplazamos los puntos medios el vector normal escalado
    newpts1 = rs.PointTransform(a,trans1)
    newpts2 = rs.PointTransform(a,trans2)
    

    
    tri = rs.AddPolyline([b,newpts1,newpts2,b])
    triangles.append(tri)
    
ptList = pts

