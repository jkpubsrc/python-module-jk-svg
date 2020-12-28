



from .AbstractSVGElement import AbstractSVGElement
from .SVGGenericElement import SVGGenericElement
from .SVGLine import SVGLine
from .SVGEllipse import SVGEllipse
from .SVGCircle import SVGCircle
from .SVGRect import SVGRect
from .SVGPolygon import SVGPolygon
from .SVGPolyline import SVGPolyline
from .SVGPath import SVGPath
from .SVGText import SVGText





class _GroupElementsMixin:

	def createElement(self, tagName:str) -> SVGGenericElement:
		assert isinstance(tagName, str)
		assert tagName

		if tagName == "path":
			return self.createPath()
		elif tagName == "line":
			return self.createLine()
		elif tagName == "ellipse":
			return self.createEllipse()
		elif tagName == "circle":
			return self.createCircle()
		elif tagName == "rect":
			return self.createRect()
		elif tagName == "polygon":
			return self.createPolygon()
		elif tagName == "polyline":
			return self.createPolyline()
		elif tagName == "text":
			return self.createText()

		ret = SVGGenericElement(tagName)
		self._children.append(ret)
		return ret
	#

	def createPath(self) -> SVGPath:
		ret = SVGPath()
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

	def createPolyline(self) -> SVGPolyline:
		ret = SVGPolyline()
		self._children.append(ret)
		return ret
	#

	def createText(self) -> SVGText:
		ret = SVGText()
		self._children.append(ret)
		return ret
	#

#






