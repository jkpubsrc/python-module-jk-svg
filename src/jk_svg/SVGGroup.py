

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from .SVGLine import SVGLine
from .SVGEllipse import SVGEllipse
from .SVGCircle import SVGCircle
from .SVGRect import SVGRect
from .SVGPolygon import SVGPolygon
from .SVGPolyline import SVGPolyline

from ._AttrMixinStyle import _AttrMixinStyle
from ._GroupElementsMixin import _GroupElementsMixin
from .Transformer import Transformer





class SVGGroup(AbstractSVGElement, _AttrMixinStyle, _GroupElementsMixin):

	def __init__(self):
		super().__init__("g")

		self.__transformer = Transformer(self._attributes.get("transform"))
		self.__transformer._connectedSVGControl = self
	#

	@property
	def transform(self) -> Transformer:
		return self.__transformer
	#

	def createGroup(self):
		ret = SVGGroup()
		self._children.append(ret)
		return ret
	#

#












