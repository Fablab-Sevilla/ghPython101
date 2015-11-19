import Rhino.Geometry as rg
import Rhino.Display as rd

#Creamos un plano con tres puntos cualesquiera
plane = rg.Plane(pts[0],pts[1],pts[2])

#Proyectamos el punto 3 sobre el plano calculado
newPt3 = plane.ClosestPoint(pts[3])

#Calculamos el desplazamiento de cada punto
dev = pts[3].DistanceTo(newPt3)

#Creamos un color HSL(float) con dev y lo transformamos en RGB
devCol = rd.ColorHSL(dev*0.9,1,0.5)
devCol = devCol.ToArgbColor()

#Sustituimos el punto 3 por su nuevo valor
pts.append(newPt3)
lines = [] #estas son las aspas

#Creamos una marca en cada panel fuera de tolerancia
if dev>T:
    
    l0 = rg.Line(pts[0],pts[2])
    l1 = rg.Line(pts[1],pts[4])
    lines.extend([l0,l1])

#Creamos la polilinea de cada panel y calculamos su area    
pol = rg.PolylineCurve((pts[0],pts[1],pts[2],pts[4],pts[0]))
#Creamos dos listas de polilineas de los paneles triangulares
pol2 = rg.PolylineCurve((pts[2],pts[3],pts[4],pts[2]))
pol3 = rg.PolylineCurve((pts[0],pts[3],pts[4],pts[0]))

areaObj = rg.AreaMassProperties.Compute(pol)
area = areaObj.Area

w = lines