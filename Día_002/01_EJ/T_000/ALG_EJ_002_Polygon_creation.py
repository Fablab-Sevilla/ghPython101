import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

pts = []

# Creates a loop to build points with polar coordinates
# at 2Pi/n increments.

for i in range(n):
    pts.append(rs.Polar(pt,i*(360.0/n),r))

pts.append(pts[0]) # Appends the first point again to close the curve

pol = rg.PolylineCurve(pts) 

# rg.PolylineCurve != rg.Polyline
# Polyline = just an ordered list of points3d
# PolylineCurve = and actual Polyline curve
    
    