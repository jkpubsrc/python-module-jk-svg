

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinXY import _AttrMixinXY
from ._AttrMixinStyle import _AttrMixinStyle
from ._AttrMixinClass import _AttrMixinClass
from ._AttrMixinTextContent import _AttrMixinTextContent






class SVGText(AbstractSVGElement, _AttrMixinXY, _AttrMixinStyle, _AttrMixinClass, _AttrMixinTextContent):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__("text")
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

	"""
	TODO
	def getBoundingPoints(self):
		yield from super().getBoundingPoints()
		x1, y1 = self.x, self.y
		yield x1, y1
	#
	"""

#












