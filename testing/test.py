#!/usr/bin/python3




from jk_svg import *






svg = SVGGraphic()

# ----

with svg.createGroup() as g:

	with  g.createLine() as line:
		line.x1 = 100
		line.y1 = 100
		line.x2 = 300
		line.y2 = 200

	with g.createPolygon() as poly:
		poly.points.append( (20, 0) )
		poly.points.append( (100, 20) )
		poly.points.append( (80, 100) )
		poly.points.append( (0, 80) )

# ----

bounds = svg.getBoundingBox()
print(bounds)

print(svg.toSVG())

# ----

svg.move(100, 100)

bounds = svg.getBoundingBox()
print(bounds)

print(svg.toSVG())





