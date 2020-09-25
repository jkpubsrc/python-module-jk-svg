

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinCXCY:

	def _init_AttrMixinCXCY(self):
		self._moveCallback = self.__move
	#

	def __move(self, dx:float, dy:float):
		self.cx += dx
		self.cy += dy
	#

	@property
	def cx(self) -> float:
		return self._attributes.get("cx", 0)
	#

	@cx.setter
	def cx(self, v:float):
		self._attributes["cx"] = v
	#

	@property
	def cy(self) -> float:
		return self._attributes.get("cy", 0)
	#

	@cy.setter
	def cy(self, v:float):
		self._attributes["cy"] = v
	#

#












