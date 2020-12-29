#!/usr/bin/python3


import os

import jk_utils

from jk_svg import *




svg = SVGGraphic()
svg.attributes["width"] = 200
svg.attributes["height"] = 200




with svg.createRect() as rect:
	rect.setBounds(0, 0, 100, 200)
	rect.style = "fill:#008000"

with svg.createRect() as rect:
	rect.setBounds(100, 0, 100, 200)
	rect.style = "fill:#000080"





with svg.defs.createMask() as mask:
	mask.id = "hole"
	mask.maskContentUnits = "objectBoundingBox"
	mask.comment = "The mask that creates the hole in the ring"

	with mask.createRect() as rect:
		rect.width = "100%"
		rect.height = "100%"
		rect.style = "fill:white"

	with mask.createCircle() as circle:
		circle.r = 0.25
		circle.cx = 0.5
		circle.cy = 0.5
		circle.style = "fill:black"

with svg.createCircle() as circle:
	circle.comment = "The circle that implements the ring"
	circle.setBounds(20, 20, 160, 160)
	circle.mask = "hole"
	circle.style = "fill:orange"



# ----

svg.writeToFile(jk_utils.fsutils.getFileNameWithoutExtension(__file__) + ".output.svg")





