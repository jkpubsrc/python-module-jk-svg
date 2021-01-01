


import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from .SVGGroup import SVGGroup
from .SVGGenericElement import SVGGenericElement
from .SVGDefs import SVGDefs
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

		self.__defs = SVGDefs()
		self._cssStyleLines = []

		self.setSizeDinA4()
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def defs(self) -> SVGDefs:
		return self.__defs
	#

	@property
	def cssStyleLines(self) -> list:
		return self._cssStyleLines
	#

	@cssStyleLines.setter
	def cssStyleLines(self, v:list):
		if v is None:
			self._cssStyleLines.clear()
		elif isinstance(v, (list,tuple)):
			self._cssStyleLines.clear()
			self._cssStyleLines.extend(v)
		else:
			raise TypeError(type(v).__name__)
	#

	@property
	def cssStyle(self) -> list:
		return "\n".join(self._cssStyleLines)
	#

	@cssStyle.setter
	def cssStyle(self, v:str):
		v = v.strip()
		self._cssStyleLines = v.split("\n")
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _toSVG(self, w:jk_hwriter.HWriter, bPretty:bool = True):

		extraChildren = []

		if self._cssStyleLines:
			svgStyle = SVGGenericElement("style")
			svgStyle._textContent = "\n" + "\n".join(self._cssStyleLines) + "\n"
			extraChildren.append(svgStyle)

		if self.__defs._children:
			extraChildren.append(self.__defs)

		super()._toSVG(w, bPretty, extraChildren)
	#

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

	def toSVG(self, bPretty:bool = True, bWithXMLDeclaration:bool = True) -> str:
		w = jk_hwriter.HWriter()
		if bWithXMLDeclaration:
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






