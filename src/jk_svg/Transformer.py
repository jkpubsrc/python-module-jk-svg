

import re



class Transformer(object):

	__slots__ = [ "_connectedSVGControl", "__translation", "__scaling" ]

	def __init__(self, v = None):
		super().__init__()

		self._connectedSVGControl = None

		self.__translation = [ 0, 0 ]
		self.__scaling = [ 1, 1 ]

		if v is not None:
			if isinstance(v, str):
				self.__parseFromStr(v)
			elif isinstance(v, Transformer):
				self.__translation = list(v.__translation)
				self.__scaling = list(v.__scaling)
			else:
				raise Exception("Unknown: " + str(type(v)))
	#

	@property
	def translateX(self) -> float:
		return self.__translation[0]
	#

	@translateX.setter
	def translateX(self, v:float):
		assert isinstance(v, (float, int))
		self.__translation[0] = v

		self.commit()
	#

	@property
	def translateY(self) -> float:
		return self.__translation[1]
	#

	@translateY.setter
	def translateY(self, v:float):
		assert isinstance(v, (float, int))
		self.__translation[1] = v

		self.commit()
	#

	@property
	def scaleX(self) -> float:
		return self.__scaling[0]
	#

	@scaleX.setter
	def scaleX(self, v:float):
		assert isinstance(v, (float, int))
		self.__scaling[0] = v

		self.commit()
	#

	@property
	def scaleY(self) -> float:
		return self.__translation[1]
	#

	@scaleX.setter
	def scaleX(self, v:float):
		assert isinstance(v, (float, int))
		self.__scaling[1] = v

		self.commit()
	#

	def commit(self):
		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["transform"] = str(self)
	#

	def reset(self):
		self.__translation = [ 0, 0 ]
		self.__scaling = [ 1, 1 ]

		self.commit()
	#

	def copy(self):
		return Transformer(self)
	#

	def __str__(self):
		return "translate({} {})".format(self.__translation[0], self.__translation[1]) \
			+ " scale({} {})".format(self.__scaling[0], self.__scaling[1])
	#

	def __parseFromStr(self, s:str):
		for m in re.finditer("(translate|scale)\(([^\)]+)\)", s):
			groupName = m.group(1)
			items = m.group(2).split(" ")
			if groupName == "translate":
				self.__translation[0] = float(items[0])
				self.__translation[1] = float(items[1])
			elif groupName == "scale":
				self.__scaling[0] = float(items[0])
				self.__scaling[1] = float(items[1])
			else:
				raise Exception()

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["transform"] = str(self)
	#

#






