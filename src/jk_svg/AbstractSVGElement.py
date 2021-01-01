

import typing
import sys
import inspect
import random

import jk_typing
import jk_hwriter

from .BoundingBox import BoundingBox
from ._AttrMixinStyle import _AttrMixinStyle
from ._AttrMixinClass import _AttrMixinClass









def _toStr(v):
	if isinstance(v, float):
		s = list("{:.14f}".format(v))			# NOTE: It doesn't make much sense to have a larger precision as typically floating point numbers are IEEE 754 format only.
		while (s[-1] == "0") and (s[-2] != "."):
			del s[-1]
		return "".join(s)
	elif isinstance(v, int):
		return str(v)
	elif isinstance(v, str):
		# TODO: perform valid XML encoding of text
		return v
	else:
		return str(v)
#







class AbstractSVGElement(_AttrMixinStyle, _AttrMixinClass):

	_SORT_ATTRIBUTES_KEY_MAP = {
		"x":		"_1_x",
		"y":		"_1_y",
		"width":	"_2_w",
		"height":	"_3_h",
		"x1":		"_4_x1",
		"y1":		"_4_y1",
		"x2":		"_5_x2",
		"y2":		"_5_y2",
		"cx":		"_6_cx",
		"cy":		"_6_cy",
		"r":		"_7_r",
		"rx":		"_8_rx",
		"ry":		"_8_ry",
	}

	################################################################################################################################
	## Constructor
	################################################################################################################################

	@jk_typing.checkFunctionSignature()
	def __init__(self, tagName:str = None):
		if not tagName:
			raise Exception("tagName missing")

		self._tagName = tagName						# str | the name of the SVG element
		self._attributes = {}						# str->any | the attributes of this SVG element
		self._children = []							# AbstractSVGElement[] | nested elements
		self._moveCallback = None					# callable | 
		self._textContent = None					# str | NOTE: element text content will be ignored if we have children.
		self._maskRef = None						# str | if set: stores a reference to a mask
		self._comment = None						# str | if set: a comment that is to be placed before a comonent in the output

		for clazz in inspect.getmro(self.__class__):
			if clazz.__name__.startswith("_AttrMixin"):
				if hasattr(clazz, "_init" + clazz.__name__):
					getattr(clazz, "_init" + clazz.__name__)(self)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def id(self) -> typing.Union[str,None]:
		return self._attributes.get("id")
	#

	@id.setter
	def id(self, v:typing.Union[str,None]):
		if v is not None:
			assert isinstance(v, str)
		self._attributes["id"] = v
	#

	@property
	def comment(self) -> typing.Union[str,None]:
		return self._comment
	#

	@comment.setter
	def comment(self, v:typing.Union[str,None]):
		if v is not None:
			assert isinstance(v, str)
		self._comment = v
	#

	@property
	def mask(self) -> typing.Union[str,None]:
		return self._maskRef
	#

	@mask.setter
	def mask(self, v:typing.Union[str,None]):
		if v is not None:
			assert isinstance(v, str)
		self._maskRef = v
	#

	@property
	def tagName(self) -> str:
		return self._tagName
	#

	@property
	def attributes(self) -> dict:
		return self._attributes
	#

	@property
	def children(self) -> list:
		return self._children
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def __sortAttributes(self, attributesDict:dict) -> list:
		sortedKeys = sorted(attributesDict.keys(), key=lambda x: AbstractSVGElement._SORT_ATTRIBUTES_KEY_MAP.get(x, x))
		return [ (k,attributesDict[k]) for k in sortedKeys ]
	#

	@jk_typing.checkFunctionSignature()
	def _toSVG(self, w:jk_hwriter.HWriter, bPretty:bool = True, extraChildren:list = None):
		# ---- get children list

		if extraChildren:
			children = list(extraChildren)
			children.extend(self._children)
		else:
			children = self._children

		# ---- prepare attributes

		self.cleanAttributes()

		attributesMap = dict(self._attributes)
		if self._maskRef:
			attributesMap["mask"] = "url(#" + self._maskRef + ")"
		sortedAttributes = self.__sortAttributes(attributesMap)

		# ---- write comment

		if bPretty:
			if self._comment:
				w.writeLn("<!-- " + self._comment + " -->")

		# ---- determine output mode

		bPrettyCompact = bPretty and not self._children

		# ---- write regular output

		if bPrettyCompact:
			# pretty, but no children

			w.write("<" + self._tagName)

			if sortedAttributes:
				for key, value in sortedAttributes:
					w.write("\t" + key + "=\"" + _toStr(value) + "\"")
				w.write("\t")

			if self._textContent:
				w.writeLn(">" + _toStr(self._textContent) + "</" + self.tagName + ">")

			else:
				w.writeLn("/>")

		elif bPretty:
			# pretty, possibly with children

			if sortedAttributes:
				w.writeLn("<" + self._tagName)
				w.incrementIndent()
				for key, value in sortedAttributes:
					w.writeLn(key + "=\"" + _toStr(value) + "\"")
				w.write(">" if (children or self._textContent) else "/>")
				w.decrementIndent()

			else:
				w.write("<" + self._tagName)
				w.write(">" if (children or self._textContent) else "/>")

			if children:
				w.writeLn()
				w.incrementIndent()

				for c in children:
					c._toSVG(w, True)

				w.decrementIndent()
				w.writeLn("</" + self._tagName + ">")

			elif self._textContent:
				w.writeLn(_toStr(self._textContent) + "</" + self.tagName + ">")

			else:
				w.writeLn()

		else:
			# optimized output for non-humans

			w.write("<" + self._tagName)

			for key, value in sortedAttributes:
				w.write(" " + key + "=\"" + _toStr(value) + "\"")

			if children:
				w.write(">")

				for c in children:
					c._toSVG(w, False)

				w.write("</" + self._tagName + ">")

			elif self._textContent:
				w.write(">" + _toStr(self._textContent) + "</" + self.tagName + ">")

			else:
				w.write("/>")
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def generateUniqueID(self, prefix:str) -> str:
		while True:
			ret = prefix + str(random.randint(1, 999999))
			bFound = False
			for c in self._children:
				if c.id == ret:
					bFound = True
					break
			if not bFound:
				return ret
	#

	def getBoundingPoints(self):
		for c in self._children:
			yield from c.getBoundingPoints()
	#

	def move(self, dx:float, dy:float):
		if self._moveCallback:
			self._moveCallback(dx, dy)
		for c in self._children:
			c.move(dx, dy)
	#

	def toSVG(self, bPretty:bool = True) -> str:
		w = jk_hwriter.HWriter()
		self._toSVG(w, bPretty)
		return str(w)
	#

	def cleanAttributes(self):
		for key in list(self._attributes.keys()):
			a = self._attributes[key]
			if (a is None) or (a is ""):
				del self._attributes[key]
	#

	def getBoundingBox(self) -> typing.Union[BoundingBox,None]:
		allX = []
		allY = []
		for px, py in self.getBoundingPoints():
			allX.append(px)
			allY.append(py)

		if allX:
			return BoundingBox(min(allX), min(allY), max(allX), max(allY))
		else:
			return None
	#

	def __enter__(self, *args):
		return self
	#

	def __exit__(self, *args):
		pass
	#

#












