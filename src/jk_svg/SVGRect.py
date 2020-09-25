

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinXY import _AttrMixinXY
from ._AttrMixinWidthHeight import _AttrMixinWidthHeight
from ._AttrMixinStyle import _AttrMixinStyle





class SVGRect(AbstractSVGElement, _AttrMixinXY, _AttrMixinWidthHeight, _AttrMixinStyle):

	def __init__(self):
		super().__init__("rect")
	#

	def getBoundingPoints(self):
		yield from super().getBoundingPoints()
		x1, y1 = self.x, self.y
		x2, y2 = x1 + self.width, y1 + self.height
		yield x1, y1
		yield x1, y2
		yield x2, y1
		yield x2, y2
	#

#











