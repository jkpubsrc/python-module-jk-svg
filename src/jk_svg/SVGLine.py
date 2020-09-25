

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinX1Y1X2Y2 import _AttrMixinX1Y1X2Y2
from ._AttrMixinStyle import _AttrMixinStyle




class SVGLine(AbstractSVGElement, _AttrMixinX1Y1X2Y2, _AttrMixinStyle):

	def __init__(self):
		super().__init__("line")
	#

	def getBoundingPoints(self):
		yield from super().getBoundingPoints()
		yield self.x1, self.y1
		yield self.x2, self.y2
	#

#












