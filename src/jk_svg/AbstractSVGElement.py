

import typing
import sys
import inspect

import jk_typing
import jk_hwriter





class AbstractSVGElement(object):

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

	def getBoundingPoints(self):
		for c in self._children:
			yield from c.getBoundingPoints()
	#

	def move(self, dx:float, dy:float):
		if self._moveCallback:
			self._moveCallback(dy, dy)
		for c in self._children:
			c.move(dx, dy)
	#

	def toSVG(self, bPretty:bool = True) -> str:
		w = jk_hwriter.HWriter()
		self._toSVG(w, bPretty)
		return str(w)
	#

	@jk_typing.checkFunctionSignature()
	def _toSVG(self, w:jk_hwriter.HWriter, bPretty:bool = True):

		if bPretty:
			if self._attributes:
				w.writeLn("<" + self._tagName)
				w.incrementIndent()
				for key, value in self._attributes.items():
					w.writeLn(key + "=\"" + str(value) + "\"")
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
				w.write(" " + key + "=\"" + str(value) + "\"")

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

	def getBoundingBox(self) -> typing.Union[tuple,None]:
		allX = []
		allY = []
		for px, py in self.getBoundingPoints():
			allX.append(px)
			allY.append(py)

		if allX:
			return min(allX), min(allY), max(allX), max(allY)
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












