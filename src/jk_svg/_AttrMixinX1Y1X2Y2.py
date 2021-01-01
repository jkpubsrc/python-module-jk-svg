

import typing

import jk_typing
import jk_hwriter






class _AttrMixinX1Y1X2Y2:

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def _init_AttrMixinX1Y1X2Y2(self):
		self._moveCallback = self.__move
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def _xy1(self) -> tuple:
		return self._attributes.get("x1", 0), self._attributes.get("y1", 0)
	#

	@_xy1.setter
	def _xy1(self, value:tuple):
		assert isinstance(value, (list,tuple))
		assert len(value) >= 2
		assert isinstance(value[0], (int,float))
		assert isinstance(value[1], (int,float))
		self._attributes["x1"] = value[0]
		self._attributes["y1"] = value[1]
	#

	@property
	def _xy2(self) -> tuple:
		return self._attributes.get("x2", 0), self._attributes.get("y2", 0)
	#

	@_xy2.setter
	def _xy2(self, value:tuple):
		assert isinstance(value, (list,tuple))
		assert len(value) >= 2
		assert isinstance(value[0], (int,float))
		assert isinstance(value[1], (int,float))
		self._attributes["x2"] = value[0]
		self._attributes["y2"] = value[1]
	#

	@property
	def x1(self) -> float:
		return self._attributes.get("x1", 0)
	#

	@x1.setter
	def x1(self, v:float):
		self._attributes["x1"] = v
	#

	@property
	def y1(self) -> float:
		return self._attributes.get("y1", 0)
	#

	@y1.setter
	def y1(self, v:float):
		self._attributes["y1"] = v
	#

	@property
	def x2(self) -> float:
		return self._attributes.get("x2", 0)
	#

	@x2.setter
	def x2(self, v:float):
		self._attributes["x2"] = v
	#

	@property
	def y2(self) -> float:
		return self._attributes.get("y2", 0)
	#

	@y2.setter
	def y2(self, v:float):
		self._attributes["y2"] = v
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def __move(self, dx:float, dy:float):
		self.x1 += dx
		self.y1 += dy
		self.x2 += dx
		self.y2 += dy
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

#












