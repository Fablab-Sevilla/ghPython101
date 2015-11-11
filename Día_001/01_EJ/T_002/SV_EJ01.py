"""Alumno: Sergi Viel
    usuario: evokraken
    version 03.00
"""
"""
CONTROL DE CAMBIOS
1-Borra y limpiar comentarios e instrucciones comentadas de versiones anteriores
2-Forzar Type Hint del componente de GH. Lin-19
3-Forzamos la variable PtoO Point3d en Type Hint del componente. Ya no tenemos
que tipificar en lineas 21, 34 y 35.

"""

import random as rd
import Rhino.Geometry as rg

#configuramos random para un seed aportado por usuario.
rd.seed(sSeed)

#punto origen aportado por usuario y acumulador de resultados
origen = (PtoO)
resultado=[]

for i in range(intN):
    #vector de recta
    VtoF = rg.Vector3d(rd.randint(-1,1),rd.randint(-1,1),0)
    
    #trazo de la recta final
    trazo=rg.Line(origen, VtoF)
    resultado.append(trazo)
    
    
    #preparamos para el siguiente bucle
    punto = (origen+VtoF)
    origen = (punto)
    
#suma de todos los trazos lo dejamos para la salida
a = resultado
