

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinCXCY import _AttrMixinCXCY
from ._AttrMixinRXRY import _AttrMixinRXRY
from ._AttrMixinStyle import _AttrMixinStyle




class SVGEllipse(AbstractSVGElement, _AttrMixinCXCY, _AttrMixinRXRY, _AttrMixinStyle):

	def __init__(self):
		super().__init__("ellipse")
	#

	def getBoundingPoints(self):
		yield from super().getBoundingPoints()
		yield self.cx - self.rx, self.cy
		yield self.cx + self.rx, self.cy
		yield self.cx, self.cy - self.ry
		yield self.cx, self.cy + self.ry
	#

#












