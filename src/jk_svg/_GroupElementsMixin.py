



from .AbstractSVGElement import AbstractSVGElement
from .SVGElement import SVGElement
from .SVGLine import SVGLine
from .SVGEllipse import SVGEllipse
from .SVGCircle import SVGCircle
from .SVGRect import SVGRect
from .SVGPolygon import SVGPolygon
from .SVGPolyline import SVGPolyline




class _GroupElementsMixin:

	def createElement(self, tagName:str) -> SVGElement:
		assert isinstance(tagName, str)
		assert tagName

		ret = SVGElement(tagName)
		self._children.append(ret)
		return ret
	#

	def createLine(self) -> SVGLine:
		ret = SVGLine()
		self._children.append(ret)
		return ret
	#

	def createEllipse(self) -> SVGEllipse:
		ret = SVGEllipse()
		self._children.append(ret)
		return ret
	#

	def createCircle(self) -> SVGCircle:
		ret = SVGCircle()
		self._children.append(ret)
		return ret
	#

	def createRect(self) -> SVGRect:
		ret = SVGRect()
		self._children.append(ret)
		return ret
	#

	def createPolygon(self) -> SVGPolygon:
		ret = SVGPolygon()
		self._children.append(ret)
		return ret
	#

#






