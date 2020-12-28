

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinStyle:

	@property
	def style(self) -> str:
		return self._attributes.get("style", 0)
	#

	@style.setter
	def style(self, v:str):
		self._attributes["style"] = v
	#

#












