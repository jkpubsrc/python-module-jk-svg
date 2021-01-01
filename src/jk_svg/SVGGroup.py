

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement

from ._GroupElementsMixin import _GroupElementsMixin
from .Transformer import Transformer
from .SVGMask import SVGMask






class SVGGroup(AbstractSVGElement, _GroupElementsMixin):

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

	def createMask(self):
		ret = SVGMask()
		self._children.append(ret)
		return ret
	#

#












