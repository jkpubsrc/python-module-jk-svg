

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinXY:

	def _init_AttrMixinXY(self):
		self._moveCallback = self.__move
	#

	def __move(self, dx:float, dy:float):
		self.x += dx
		self.y += dy
	#

	@property
	def x(self) -> float:
		return self._attributes.get("x", 0)
	#

	@x.setter
	def x(self, v:float):
		self._attributes["x"] = v
	#

	@property
	def y(self) -> float:
		return self._attributes.get("y", 0)
	#

	@y.setter
	def y(self, v:float):
		self._attributes["y"] = v
	#

#












