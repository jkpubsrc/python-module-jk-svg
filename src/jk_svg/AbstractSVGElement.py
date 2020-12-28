

import typing
import sys
import inspect

import jk_typing
import jk_hwriter

from .BoundingBox import BoundingBox









def _toStr(v):
	if isinstance(v, float):
		s = list("{:.14f}".format(v))			# NOTE: It doesn't make much sense to have a larger precision as typically floating point numbers are IEEE 754 format only.
		while s[-1] == "0":
			del s[-1]
		return "".join(s)
	elif isinstance(v, int):
		return str(v)
	elif isinstance(v, str):
		return v
	else:
		return str(v)
#








class AbstractSVGElement(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	@jk_typing.checkFunctionSignature()
	def __init__(self, tagName:str = None):
		if not tagName:
			raise Exception("tagName missing")

		self._tagName = tagName
		self._attributes = {}
		self._children = []
		self._text = None
		self._moveCallback = None

		for clazz in inspect.getmro(self.__class__):
			if clazz.__name__.startswith("_AttrMixin"):
				if hasattr(clazz, "_init" + clazz.__name__):
					getattr(clazz, "_init" + clazz.__name__)(self)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def id(self) -> str:
		return self._attributes.get("id", 0)
	#

	@id.setter
	def id(self, v:float):
		self._attributes["id"] = v
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

	@jk_typing.checkFunctionSignature()
	def _toSVG(self, w:jk_hwriter.HWriter, bPretty:bool = True):

		self.cleanAttributes()

		if bPretty:
			if self._attributes:
				w.writeLn("<" + self._tagName)
				w.incrementIndent()
				for key, value in self._attributes.items():
					w.writeLn(key + "=\"" + _toStr(value) + "\"")
				w.write(">" if (self._children or self._text) else "/>")
				w.decrementIndent()

			else:
				w.write("<" + self._tagName)
				w.write(">" if (self._children or self._text) else "/>")

			if self._children:
				w.writeLn()
				w.incrementIndent()

				for c in self._children:
					c._toSVG(w, True)

				w.decrementIndent()
				w.writeLn("</" + self._tagName + ">")

			elif self._text:
				w.writeLn(self._text + "</" + self.tagName + ">")

			else:
				w.writeLn()

		else:
			w.write("<" + self._tagName)

			for key, value in self._attributes.items():
				w.write(" " + key + "=\"" + _toStr(value) + "\"")

			if self._children:
				w.write(">")

				for c in self._children:
					c._toSVG(w, False)

				w.write("</" + self._tagName + ">")

			elif self._text:
				w.write(">" + self._text + "</" + self.tagName + ">")

			else:
				w.write("/>")
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

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












