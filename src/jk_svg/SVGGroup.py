

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement

from ._AttrMixinStyle import _AttrMixinStyle
from ._GroupElementsMixin import _GroupElementsMixin
from .Transformer import Transformer





class SVGGroup(AbstractSVGElement, _AttrMixinStyle, _GroupElementsMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__("g")

		self.__transformer = Transformer(self._attributes.get("transform"))
		self.__transformer._connectedSVGControl = self
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def transform(self) -> Transformer:
		return self.__transformer
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def createGroup(self):
		ret = SVGGroup()
		self._children.append(ret)
		return ret
	#

#












