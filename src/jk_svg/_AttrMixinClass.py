

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinClass:

	@property
	def clazz(self) -> str:
		return self._attributes.get("class", 0)
	#

	@clazz.setter
	def clazz(self, v:str):
		self._attributes["class"] = v
	#

#












