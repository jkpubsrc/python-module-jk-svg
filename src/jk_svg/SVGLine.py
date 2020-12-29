

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinX1Y1X2Y2 import _AttrMixinX1Y1X2Y2
from ._AttrMixinStyle import _AttrMixinStyle




class SVGLine(AbstractSVGElement, _AttrMixinX1Y1X2Y2, _AttrMixinStyle):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__("line")
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
		yield self.x1, self.y1
		yield self.x2, self.y2
	#

	def setBounds(self, x, y, width, height):
		self.x1 = x
		self.y1 = y
		self.x2 = x + width
		self.y2 = y + height
	#

	def getBounds(self) -> list:
		return [ self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1 ]
	#

#












