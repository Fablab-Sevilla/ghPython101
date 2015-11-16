import Rhino.Geometry as rg
from Grasshopper import DataTree as Tree
from Grasshopper.Kernel.Data import GH_Path as Path


def planarize(pts,T):
    
    '''
    Creates a planar quad panel from a serie of 4 points projecting one of
    those over a plane defined by the other 3 points.
    '''
    
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

        w = lines


ptList = []
polList = []

#Initializing an empty data tree
ptTree = Tree[object]()

for i in range(uDiv+1):
    ptListTemp = []
    
    for j in range(vDiv+1):
        
        ptTemp = srf.Evaluate(i/uDiv,j/vDiv,2)[1]
        ptListTemp.append(ptTemp)
        
    ptList.append(ptListTemp)
    
counter = 0
for i in range(uDiv):
    for j in range(vDiv):
        
        pt0 = ptList[i][j]
        pt1 = ptList[i+1][j]
        pt2 = ptList[i][j+1]
        pt3 = ptList[i+1][j+1]
        
        # Adding points to datatree
        # The commented lines produce the flipped tree.
        #ptTree.Add(pt0,Path(0))
        #ptTree.Add(pt1,Path(1))
        #ptTree.Add(pt2,Path(2))
        #ptTree.Add(pt3,Path(3))
        
        ptTree.AddRange([pt0,pt1,pt3,pt2],Path(counter))
        counter += 1
        
        polList.append(rg.Polyline([pt0,pt1,pt3,pt2,pt0]))
        
for  i in range(ptTree.BranchCount):
    
    planarize(ptTree.Branch(Path(i)),tol)
        
        
        
panel = polList    