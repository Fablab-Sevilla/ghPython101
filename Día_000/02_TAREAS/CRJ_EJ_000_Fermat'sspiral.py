#importar librerias
import rhinoscriptsyntax as rs
import math as m
import ghpythonlib.components as gh

#lista vacia puntos
listPts = []
#radio esfera
r = C*m.sqrt((It-1)*Alpha) 

#bucle espiral-esfera
for i in range(It):
    angTheta = i*Alpha
    rh = C*m.sqrt(angTheta)
    pt = rs.Polar(ptB,angTheta,rh)
    #lista puntos planos
    listPts.append(pt)
    
    #rv = sqrt(r^2-rh^2) pitágoras
    rv = m.sqrt(m.pow(r,2)-m.pow(rh,2))
    #sustituir la Z de cada punto por su rv
    listPts[i].Z=rv
    print listPts

Pts = listPts 
#vor = gh.Voronoi(Pts,rad)
