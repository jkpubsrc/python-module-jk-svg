


import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from .SVGLine import SVGLine
from .SVGEllipse import SVGEllipse
from .SVGCircle import SVGCircle
from .SVGRect import SVGRect
from .SVGPolygon import SVGPolygon
from .SVGGroup import SVGGroup
from .SVGPolyline import SVGPolyline
from ._GroupElementsMixin import _GroupElementsMixin
from ._AttrMixinWidthHeight import _AttrMixinWidthHeight





class SVGGraphic(AbstractSVGElement, _GroupElementsMixin, _AttrMixinWidthHeight):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__("svg")
		self._attributes["xmlns:svg"] = "http://www.w3.org/2000/svg"
		self._attributes["version"] = "1.1"

		self.setSizeDinA4()
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

	def setSizeDinA0(self):
		self._attributes["width"] = "841mm"
		self._attributes["height"] = "1189mm"
	#

	def setSizeDinA1(self):
		self._attributes["width"] = "594mm"
		self._attributes["height"] = "841mm"
	#

	def setSizeDinA2(self):
		self._attributes["width"] = "420mm"
		self._attributes["height"] = "594mm"
	#

	def setSizeDinA3(self):
		self._attributes["width"] = "297mm"
		self._attributes["height"] = "420mm"
	#

	def setSizeDinA4(self):
		self._attributes["width"] = "210mm"
		self._attributes["height"] = "297mm"
	#

	def setSizeDinA5(self):
		self._attributes["width"] = "148mm"
		self._attributes["height"] = "210mm"
	#

	def setSizeDinA6(self):
		self._attributes["width"] = "105mm"
		self._attributes["height"] = "148mm"
	#

	def setSizeDinA7(self):
		self._attributes["width"] = "74mm"
		self._attributes["height"] = "105mm"
	#

	def setSizeDinA8(self):
		self._attributes["width"] = "52mm"
		self._attributes["height"] = "74mm"
	#

	def setSizeDinA9(self):
		self._attributes["width"] = "37mm"
		self._attributes["height"] = "52mm"
	#

	def toSVG(self, bPretty:bool = True) -> str:
		w = jk_hwriter.HWriter()
		w.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
		if bPretty:
			w.writeLn()
		self._toSVG(w, bPretty)
		return str(w)
	#

	def createGroup(self) -> SVGGroup:
		ret = SVGGroup()
		self._children.append(ret)
		return ret
	#

	def writeToFile(self, filePath:str):
		with open(filePath, "w") as f:
			f.write(self.toSVG())
	#

#






