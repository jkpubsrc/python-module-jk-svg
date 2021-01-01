

import typing

import jk_typing
import jk_hwriter





class _AttrMixinCXCY:

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def _init_AttrMixinCXCY(self):
		self._moveCallback = self.__move
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def _xy(self) -> tuple:
		return self._attributes.get("cx", 0), self._attributes.get("cy", 0)
	#

	@_xy.setter
	def _xy(self, value:tuple):
		assert isinstance(value, (list,tuple))
		assert len(value) >= 2
		assert isinstance(value[0], (int,float))
		assert isinstance(value[1], (int,float))
		self._attributes["cx"] = value[0]
		self._attributes["cy"] = value[1]
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

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def __move(self, dx:float, dy:float):
		self.cx += dx
		self.cy += dy
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def setCenter(self, cx, cy):
		self.cx = cx
		self.cy = cy
	#

	def getCenter(self) -> list:
		return [ self.cx, self.cy ]
	#

#












