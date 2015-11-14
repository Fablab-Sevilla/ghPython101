"""Alumno: Sergi Viel
    usuario: evokraken
    version 04.00
"""
"""
CONTROL DE CAMBIOS

La direccion se controla mediante un giro aleatorio 'cabeceo'.
El modulo controlado por un random de cero a 'magnitDePaso'.
Obtenemos el punto medio de cada paso. Trazamos un vector perpendicular
y a partir de el obtenemos dos puntos mas para cerra una celosia con los
puntos del siguiente paso. Debemos dejar dos variables en memoria de ciclo

"""

import random as rd
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

#configuramos random para un seed aportado por usuario.
rd.seed(sSeed)

#punto pUno aportado por usuario y acumulador de resultados
pUno = (PtoO)
resultado=[]
VtoF = rg.Vector3d(1,1,0)
axisZ = rg.Vector3d(0,0,1)

for i in range(intN):
    #vector de recta
    #VtoF = rg.Vector3d(rd.randint(-1,1),rd.randint(-1,1),0)
    radian = rd.randrange(-cabeceo,cabeceo,1)
    modulo = rd.randrange(1, magnitDePaso+1, 1)
    VtoFF = modulo*rs.VectorUnitize((rs.VectorRotate(VtoF,radian,axisZ)))
    VtoNormal = 0.5*rs.VectorRotate(VtoFF,90,axisZ)
    
    #Obtenemos recta 'trazoEje' y los puntos a conectar
    trazoEje = rg.Line(pUno,VtoFF)
    pDos = (trazoEje).To
    pMed = rg.Line(pUno,VtoFF).PointAt(0.5)
    pTres = rg.Line(pMed,VtoNormal).To
    pCuatro = rg.Line(pMed,-VtoNormal).To

    #Polilinea cerrada de cada paso con los puntos obtenidos
    poli = rg.Polyline([pUno,pTres,pDos,pCuatro,pUno])
    
    
    #obtenemos los resultados de cada paso
    resultado.append(trazoEje)
    resultado.append(poli)
    #resultado.append(pDos)
    #resultado.append(pMed)
    #resultado.append(pTres)
    #resultado.append(pCuatro)
    
    #excluimos en el bucle el primer y ultimo paso para esta linea
    #para evitar introducir en la lista resultado elementos vacíos
    #que puedan provocar errores.
    if i != 0 or i==intN:
        nexo1 = rg.Line(pTresPrima, pTres)
        nexo2 = rg.Line(pCuatroPrima, pCuatro)
        resultado.append(nexo1)
        resultado.append(nexo2)
    
    #preparamos para el siguiente bucle
    pTresPrima = pTres
    pCuatroPrima = pCuatro
    pUno = (pUno+VtoFF) #el inicio del trazo en el final del anterior
    VtoF = VtoFF #la direccion del anterior a partir del cual se genera el nuevo
    
#suma de todos los trazos lo dejamos para la salida
a = resultado
