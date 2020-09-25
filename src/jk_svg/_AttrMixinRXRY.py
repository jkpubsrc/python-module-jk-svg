

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinRXRY:

	@property
	def rx(self) -> float:
		return self._attributes.get("rx", 0)
	#

	@rx.setter
	def rx(self, v:float):
		self._attributes["rx"] = v
	#

	@property
	def ry(self) -> float:
		return self._attributes.get("ry", 0)
	#

	@ry.setter
	def ry(self, v:float):
		self._attributes["ry"] = v
	#

#











