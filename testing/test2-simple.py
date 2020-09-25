#!/usr/bin/python3




from jk_svg import *




STYLE_RED = "opacity:1;fill:none;fill-opacity:1;stroke:#c00000;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
STYLE_GREEN = "opacity:1;fill:none;fill-opacity:1;stroke:#008000;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
STYLE_BLUE = "opacity:1;fill:none;fill-opacity:1;stroke:#0000c0;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
STYLE_BACKGROUND = "opacity:1;fill:#a0a0a0;fill-opacity:1;stroke:none;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"


svg = SVGGraphic()

# ----

with svg.createGroup() as g:

	with g.createLine() as line:
		line.style = STYLE_GREEN
		line.x1 = 100
		line.y1 = 100
		line.x2 = 300
		line.y2 = 200

	with g.createEllipse() as ellipse:
		ellipse.style = STYLE_BLUE
		ellipse.cx = 250
		ellipse.cy = 140
		ellipse.rx = 75
		ellipse.ry = 50

	with g.createPolygon() as poly:
		poly.style = STYLE_RED
		poly.points.append( (20, 0) )
		poly.points.append( (100, 20) )
		poly.points.append( (80, 100) )
		poly.points.append( (0, 80) )
		poly.move(100, 100)

# ----

svg.writeToFile("test2.svg")





