

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinXY import _AttrMixinXY
from ._AttrMixinWidthHeight import _AttrMixinWidthHeight
from .BoundingBox import BoundingBox






class SVGRect(AbstractSVGElement, _AttrMixinXY, _AttrMixinWidthHeight):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__("rect")
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
		x1, y1 = self.x, self.y
		x2, y2 = x1 + self.width, y1 + self.height
		yield x1, y1
		yield x1, y2
		yield x2, y1
		yield x2, y2
	#

	def setBounds(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	#

	def getBounds(self) -> list:
		return [ self.x, self.y, self.width, self.height ]
	#

#












