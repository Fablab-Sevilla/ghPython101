"""Alumno: Sergi Viel
    usuario: evokraken
    version 02.00
"""
"""
CONTROL DE CAMBIOS
1-Desabilitamos las bibliotecas que no estamos usando. Usamos # coment. Lin-15
2-Usamos el metodo randint(), e inhabilitamos la funcion aMod(). Inhabilitamos
la funcion con comentario. Lin-20
3-Incluimos la obtencion de variables del vector y obtenemos directamente el vector
saltandonos un paso. Lin 39-40 incluidas en Lin 43.

"""

#importamos bibliotecas
#import rhinoscriptsyntax as rs
import random as rd
import Rhino.Geometry as rg

#creamos una función que nos crea el módulo aleatorio a valores regulados
###def aMod(valor):
###    #print valor
###    if valor <= 0.3:
###        return -1
###    elif valor > 0.3 and valor <= 0.6:
###        return 0
###    else:
###        return 1

#configuramos random para un seed aportado por usuario.
rd.seed(int(sSeed))

#punto origen aportado por usuario y acumulador de resultados
origen = rg.Point3d(PtoO)
resultado=[]

for i in range(intN):
    #coordenadas de vector
    #vx= rd.randint(-1,1)
    #vy= rd.randint(-1,1)
    
    #vector de recta
    VtoF = rg.Vector3d(rd.randint(-1,1),rd.randint(-1,1),0)
    
    #trazo de la recta final
    trazo=rg.Line(origen, VtoF)
    resultado.append(trazo)
    
    
    #preparamos para el siguiente bucle
    punto = rg.Point3d(origen+VtoF)
    origen = rg.Point3d(punto)
    
#suma de todos los trazos lo dejamos para la salida
a = resultado
