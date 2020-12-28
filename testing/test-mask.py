#!/usr/bin/python3


import os

from jk_svg import *




STYLE_RED = "opacity:1;fill:none;fill-opacity:1;stroke:#c00000;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
STYLE_GREEN = "opacity:1;fill:none;fill-opacity:1;stroke:#008000;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
STYLE_BLUE = "opacity:1;fill:none;fill-opacity:1;stroke:#0000c0;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
STYLE_BACKGROUND = "opacity:1;fill:#a0a0a0;fill-opacity:1;stroke:none;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"


svg = SVGGraphic()
svg.attributes["width"] = 200
svg.attributes["height"] = 200

with svg.createGroup() as g:
	createCheckerboard(g, 200, 200, 20, 20)

with svg.createGroup() as g:
	createRing(g, 100, 100, 100, 50)

"""
with svg.defs.createMask() as mask:
	mask.id = "hole"

	with mask.createRect() as rect:
		rect.width = "100%"
		rect.height = "100%"
		rect.style = "fill:white"

	with mask.createCircle() as circle:
		circle.r = "50"
		circle.cx = "100"
		circle.cy = "100"
		circle.style = "fill:black"

with svg.createCircle() as circle:
	circle.r = "100"
	circle.cx = "100"
	circle.cy = "100"
	circle.mask = "hole"
	circle.style = "fill:orange"
"""

svg.writeToFile(os.path.basename(__file__) + ".svg")





