

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinWidthHeight:

	@property
	def width(self) -> float:
		return self._attributes.get("width", 0)
	#

	@width.setter
	def width(self, v:float):
		self._attributes["width"] = v
	#

	@property
	def height(self) -> float:
		return self._attributes.get("height", 0)
	#

	@height.setter
	def height(self, v:float):
		self._attributes["height"] = v
	#

#












