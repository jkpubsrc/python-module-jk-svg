



import jk_utils

from .UnitValue import UnitValue




"""
class BoundingBox(tuple):

	def __new__(cls, *args):
		assert len(args) == 4
		for i in range(0, 4):
			assert isinstance(args[i], (float, int))
		return super(BoundingBox, cls).__new__(cls, tuple(args))
	#

#
"""




class BoundingBox(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, *args):
		if len(args) == 1:
			args = list(args[0])
			assert len(args) == 4
		elif len(args) == 4:
			pass
		else:
			raise Exception("Arguments invalid!")

		minX, minY, maxX, maxY = args
		assert isinstance(minX, (float, int, UnitValue))
		assert isinstance(minY, (float, int, UnitValue))
		assert isinstance(maxX, (float, int, UnitValue))
		assert isinstance(maxY, (float, int, UnitValue))

		self.__minX = minX
		self.__maxX = maxX
		self.__minY = minY
		self.__maxY = maxY
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def x(self) -> float:
		return self.__minX
	#

	@property
	def y(self) -> float:
		return self.__minY
	#

	@property
	def width(self) -> float:
		return self.__maxX - self.__minX
	#

	@property
	def height(self) -> float:
		return self.__maxY - self.__minY
	#

	@property
	def minX(self) -> float:
		return self.__minX
	#

	@minX.setter
	def minX(self, v:float):
		assert isinstance(v, (float, int))
		self.__minX = v
	#

	@property
	def maxX(self) -> float:
		return self.__maxX
	#

	@maxX.setter
	def maxX(self, v:float):
		assert isinstance(v, (float, int))
		self.__maxX = v
	#

	@property
	def minY(self) -> float:
		return self.__minY
	#

	@minY.setter
	def minY(self, v:float):
		assert isinstance(v, (float, int))
		self.__minY = v
	#

	@property
	def maxY(self) -> float:
		return self.__maxY
	#

	@maxY.setter
	def maxY(self, v:float):
		assert isinstance(v, (float, int))
		self.__maxY = v
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __getitem__(self, index):
		assert isinstance(index, int)
		if (index < 0) and (index > -4):
			index = index % 4
		assert index in ( 0, 1, 2, 3 )
		if index == 0:
			return self.__minX
		if index == 1:
			return self.__minY
		if index == 2:
			return self.__maxX
		if index == 3:
			return self.__maxY
		raise jk_utils.ImplementationError()
	#

	def __setitem__(self, index, value):
		assert isinstance(index, int)
		if (index < 0) and (index > -4):
			index = index % 4
		assert index in ( 0, 1, 2, 3 )
		assert isinstance(value, (float, int))
		if index == 0:
			self.__minX = value
		if index == 1:
			self.__minY = value
		if index == 2:
			self.__maxX = value
		if index == 3:
			self.__maxY = value
		raise jk_utils.ImplementationError()
	#

	def __str__(self):
		return "BoundingBox({}, {}, {}, {})".format(self.__minX, self.__minY, self.__maxX, self.__maxY)
	#

	def __eq__(self, other):
		if isinstance(other, BoundingBox):
			return (self.__minX == other.__minX) \
				and (self.__minY == other.__minY) \
				and (self.__maxX == other.__maxX) \
				and (self.__maxY == other.__maxY)
		elif isinstance(other, (tuple, list)):
			assert len(other) == 4
			other_minX, other_minY, other_maxX, other_maxY = other
			return (self.__minX == other_minX) \
				and (self.__minY == other_minY) \
				and (self.__maxX == other_maxX) \
				and (self.__maxY == other_maxY)
		else:
			raise Exception()
	#

	def __ne__(self, other):
		if isinstance(other, BoundingBox):
			return (self.__minX != other.__minX) \
				or (self.__minY != other.__minY) \
				or (self.__maxX != other.__maxX) \
				or (self.__maxY != other.__maxY)
		elif isinstance(other, (tuple, list)):
			assert len(other) == 4
			other_minX, other_minY, other_maxX, other_maxY = other
			return (self.__minX != other_minX) \
				or (self.__minY != other_minY) \
				or (self.__maxX != other_maxX) \
				or (self.__maxY != other_maxY)
		else:
			raise Exception()
	#

	def union(self, other):
		assert isinstance(other, BoundingBox)

		minX = min(other.__minX, self.__minX)
		minY = min(other.__minY, self.__minY)
		maxX = max(other.__maxX, self.__maxX)
		maxY = max(other.__maxY, self.__maxY)

		return BoundingBox(minX, minY, maxX, maxY)
	#

	def intersection(self, other):
		assert isinstance(other, BoundingBox)

		minX = max(other.__minX, self.__minX)
		minY = max(other.__minY, self.__minY)
		maxX = min(other.__maxX, self.__maxX)
		maxY = min(other.__maxY, self.__maxY)
		if (maxX >= minX) and (maxY >= minY):
			return BoundingBox(minX, minY, maxX, maxY)
		else:
			return None
	#

	def expand(self, *args):
		if len(args) == 1:
			assert isinstance(args[0], (float, int, UnitValue))
			nLeft = nTop = nRight = nBottom = args[0]
		elif len(args) == 4:
			nLeft, nTop, nRight, nBottom = args
			assert isinstance(nLeft, (float, int, UnitValue))
			assert isinstance(nTop, (float, int, UnitValue))
			assert isinstance(nRight, (float, int, UnitValue))
			assert isinstance(nBottom, (float, int, UnitValue))
		else:
			raise Exception("Arguments invalid!")

		self.__minX -= nLeft
		self.__maxX += nRight
		self.__minY -= nTop
		self.__maxY += nBottom
	#

	################################################################################################################################
	## Static Methods
	################################################################################################################################

	@staticmethod
	def uniteMany(*args):
		for arg in args:
			assert isinstance(arg, BoundingBox)

		minX = min([ o.__minX for o in args ])
		minY = min([ o.__minY for o in args ])
		maxX = max([ o.__maxX for o in args ])
		maxY = max([ o.__maxY for o in args ])

		return BoundingBox(minX, minY, maxX, maxY)
	#

	@staticmethod
	def intersectMany(*args):
		for arg in args:
			assert isinstance(arg, BoundingBox)

		minX = max([ o.__minX for o in args ])
		minY = max([ o.__minY for o in args ])
		maxX = min([ o.__maxX for o in args ])
		maxY = min([ o.__maxY for o in args ])

		if (maxX >= minX) and (maxY >= minY):
			return BoundingBox(minX, minY, maxX, maxY)
		else:
			return None
	#

#



















