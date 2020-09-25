

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




class SVGGroup(AbstractSVGElement, _AttrMixinStyle, _GroupElementsMixin):

	def __init__(self):
		super().__init__("g")
	#

	def createGroup(self):
		ret = SVGGroup()
		self._children.append(ret)
		return ret
	#

#












