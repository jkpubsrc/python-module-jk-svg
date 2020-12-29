

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinCXCY import _AttrMixinCXCY
from ._AttrMixinRXRY import _AttrMixinRXRY
from ._AttrMixinStyle import _AttrMixinStyle




class SVGEllipse(AbstractSVGElement, _AttrMixinCXCY, _AttrMixinRXRY, _AttrMixinStyle):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__("ellipse")
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def getBoundingPoints(self):
		yield from super().getBoundingPoints()
		yield self.cx - self.rx, self.cy
		yield self.cx + self.rx, self.cy
		yield self.cx, self.cy - self.ry
		yield self.cx, self.cy + self.ry
	#

	def setBounds(self, x, y, width, height):
		self.rx = width / 2
		self.cx = x + self.rx
		self.ry = height / 2
		self.cy = y + self.ry
	#

	def getBounds(self) -> list:
		x = self.cx - self.rx
		y = self.cy - self.ry
		w = self.rx * 2
		h = self.ry * 2
		return [ x, y, w, h ]
	#

#












