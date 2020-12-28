

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinCXCY import _AttrMixinCXCY
from ._AttrMixinR import _AttrMixinR
from ._AttrMixinStyle import _AttrMixinStyle



class SVGCircle(AbstractSVGElement, _AttrMixinCXCY, _AttrMixinR, _AttrMixinStyle):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__("circle")
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
		yield self.cx - self.r, self.cy
		yield self.cx + self.r, self.cy
		yield self.cx, self.cy - self.r
		yield self.cx, self.cy + self.r
	#

#












