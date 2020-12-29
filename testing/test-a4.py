#!/usr/bin/python3


import os

import jk_utils

from jk_svg import *






svg = SVGGraphic()
svg.setSizeDinA4()



zero = UnitValue(0, "mm")
w = UnitValue(210, "mm")
h = UnitValue(297, "mm")

xa1 = zero + 10
ya1 = zero + 10
xa2 = w - 10
ya2 = h - 10

xb1 = xa1 + 10
yb1 = ya1 + 10
xb2 = xa2 - 10
yb2 = ya2 - 10


wHalf = w/2
hHalf = h/2


with svg.createRect() as rect:
	rect.x = zero
	rect.y = zero
	rect.width = w
	rect.height = h
	rect.style = "fill:orange"


with svg.createRect() as rect:
	rect.x = xa1
	rect.y = ya1
	rect.width = xa2 - xa1
	rect.height = ya2 - ya1
	rect.style = "fill:yellow"


with svg.createRect() as rect:
	rect.x = xb1
	rect.y = yb1
	rect.width = xb2 - xb1
	rect.height = yb2 - yb1
	rect.style = "fill:#800000"

with svg.createRect() as rect:
	rect.x = zero
	rect.y = zero
	rect.width = wHalf
	rect.height = hHalf
	rect.style = "fill:#808000"



# ----

svg.writeToFile(jk_utils.fsutils.getFileNameWithoutExtension(__file__) + ".output.svg")





