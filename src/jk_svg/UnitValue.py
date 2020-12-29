


import typing








class UnitValue(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, value:typing.Union[int,float], unit:typing.Union[str,None]):
		assert isinstance(value, (int,float))
		if unit is not None:
			assert isinstance(unit, str)
			if not unit:
				unit = None

		self.__value = value
		self.__unit = unit
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def value(self) -> typing.Union[int,float]:
		return self.__value
	#

	@value.setter
	def value(self, v:typing.Union[int,float]):
		assert isinstance(v, (int,float))
		self.__value = v
	#

	@property
	def unit(self) -> typing.Union[str,None]:
		return self.__unit
	#

	@unit.setter
	def unit(self, v:typing.Union[str,None]):
		if v is not None:
			assert isinstance(v, str)
			if not v:
				v = None
		self.__unit = v
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self):
		s = list("{:.14f}".format(self.__value))
		while (s[-1] == "0") and (s[-2] != "."):
			del s[-1]
		if self.__unit:
			s.append(self.__unit)
		return "".join(s)
	#

	def __float__(self):
		return float(self.__value)
	#

	def __int__(self):
		return int(self.__value)
	#

	def __add__(self, other):
		if isinstance(other, (float,int)):
			return UnitValue(self.__value + other, self.__unit)
		elif isinstance(other, UnitValue):
			assert other.__unit == self.__unit
			return UnitValue(self.__value + other.__value, self.__unit)
		else:
			raise TypeError(type(other).__name__)
	#

	def __sub__(self, other):
		if isinstance(other, (float,int)):
			return UnitValue(self.__value - other, self.__unit)
		elif isinstance(other, UnitValue):
			assert other.__unit == self.__unit
			return UnitValue(self.__value - other.__value, self.__unit)
		else:
			raise TypeError(type(other).__name__)
	#

	def __truediv__(self, dividend):
		assert isinstance(dividend, (float,int))
		return UnitValue(self.__value / dividend, self.__unit)
	#

	def __floordiv__(self, dividend):
		assert isinstance(dividend, (float,int))
		return UnitValue(self.__value / dividend, self.__unit)
	#

	def __mul__(self, factor):
		assert isinstance(factor, (float,int))
		return UnitValue(self.__value * factor, self.__unit)
	#

#






