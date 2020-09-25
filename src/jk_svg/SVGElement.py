

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinStyle import _AttrMixinStyle



class SVGElement(AbstractSVGElement, _AttrMixinStyle):

	def __init__(self, tagName:str):
		super().__init__(tagName)
	#

#












