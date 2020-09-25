

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from .PointsList import PointsList




class _AttrMixinPoints:

	def _init_AttrMixinPoints(self):
		self._points = PointsList(self._attributes.get("points"))
		self._points._connectedSVGControl = self
		self._moveCallback = self.__move
	#

	def __move(self, dx:float, dy:float):
		temp = []
		for x, y in self._points:
			temp.append( (x + dx, y + dy) )

		self._points.clear()
		self._points.extend(temp)
	#

	@property
	def points(self) -> PointsList:
		return self._points
	#

#












