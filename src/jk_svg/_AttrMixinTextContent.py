

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinTextContent:

	@property
	def textContent(self) -> str:
		return self._textContent
	#

	@textContent.setter
	def textContent(self, v:str):
		self._textContent = v
	#

#












