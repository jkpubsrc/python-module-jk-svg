

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinCXCY import _AttrMixinCXCY
from ._AttrMixinRXRY import _AttrMixinRXRY
from ._AttrMixinStyle import _AttrMixinStyle




class SVGPath(AbstractSVGElement, _AttrMixinStyle):

	def __init__(self):
		super().__init__("path")
	#

	"""
	TODO
	def getBoundingPoints(self):
		yield from super().getBoundingPoints()
		yield self.cx - self.rx, self.cy
		yield self.cx + self.rx, self.cy
		yield self.cx, self.cy - self.ry
		yield self.cx, self.cy + self.ry
	#
	"""

#












