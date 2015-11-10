#importamos bibliotecas
import rhinoscriptsyntax as rs
import random as rd
import Rhino.Geometry as rg

#creamos una función que nos crea el módulo aleatorio a valores regulados
def aMod(valor):
    #print valor
    if valor <= 0.3:
        return -1
    elif valor > 0.3 and valor <= 0.6:
        return 0
    elif valor > 0.6:
        return 1
    else:
        #No debe salir nunca este mensaje, es como control de error
        print ("Entrada fuera de rango")

#configuramos random para un seed aportado por usuario.
rd.seed(int(sSeed))

#punto origen aportado por usuario y un objeto acumulador de los trazos
origen = rg.Point3d(PtoO)
resultado=[]

for i in range(intN):
    #coordenadas de vector
    vx= aMod(rd.random())
    vy= aMod(rd.random())
    
    #vector de recta
    VtoF = rg.Vector3d(vx,vy,0)
    
    #trazo de la recta final
    trazo=rg.Line(origen, VtoF)
    #acumulamos el resultado para la salida final
    resultado.append(trazo)
    
    
    #preparamos para el siguiente bucle
    punto = rg.Point3d(origen+VtoF)
    origen = rg.Point3d(punto)
    
#suma de todos los trazos lo dejamos preparado para la salida
a = resultado
