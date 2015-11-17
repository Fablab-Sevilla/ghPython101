import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

#Creamos un plano con tres puntos cualesquiera
plane = rg.Plane(pts[0],pts[1],pts[2])

#Proyectamos el punto 3 sobre el plano calculado
newPt3 = plane.ClosestPoint(pts[3])

#Calculamos el desplazamiento de cada punto
dev = pts[3].DistanceTo(newPt3)

#Sustituimos el punto 3 por su nuevo valor
pts[3] = newPt3
lines = []

#Creamos una marca en cada panel fuera de tolerancia
if dev>T:
    
    l0 = rg.Line(pts[0],pts[2])
    l1 = rg.Line(pts[1],pts[3])
    lines.extend([l0,l1])

#Creamos la polilinea de cada panel y calculamos su area    
pol = rg.PolylineCurve((pts[0],pts[1],pts[2],pts[3],pts[0]))

areaObj = rg.AreaMassProperties.Compute(pol)
area = areaObj.Area

a = pts
w = lines