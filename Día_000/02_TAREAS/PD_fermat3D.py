import rhinoscriptsyntax as rs
import Grasshopper as gs
import Rhino.Geometry as rg
import math as m 

auxPt = []
azilist = []


for i in range(It):
    angTheta = i*Alpha
    pt= rs.Polar(ptB, angTheta, C*m.sqrt(angTheta))
    
    #-------Hasta aquí Fermat ------
    
    #Sacamos angulos de giro ''azi'' para cada punto entre 0-sphere siendo sphere <=90
    azi =(-m.sqrt(angTheta/(It*Alpha)))*sphere
    
    #Sacamos la normal ''axis''a cada punto (multiplicando el vector del punto al origen por el z)
    v1 = rs.VectorCreate(ptB,pt)
    vz = rs.VectorCreate((0,0,0),(0,0,1))
    
    axis = rs.VectorCrossProduct(v1,vz)
    
    #Creamos la transformación giro azi grados alrededor del eje axis en el punto origen
    
    transform = rs.XformRotation2(azi,axis,ptB)
    
    pts = rs.PointTransform(pt,transform)
    
    #recogemos todos los puntos en una lista
    auxPt.append(pts)
    

    
a= auxPt

b = auxPt [1:]
