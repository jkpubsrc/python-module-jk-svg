




class PointsList(list):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, v = None):
		super().__init__()

		self._connectedSVGControl = None

		if v is not None:
			if isinstance(v, str):
				self.__parseAddPoints(v)
			elif isinstance(v, (PointsList,tuple,list)):
				self.extend(v)
			else:
				raise Exception("Unknown: " + str(type(v)))
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def __parseAddPoints(self, s:str):
		sPoints = s.spit(" ")
		for sPoint in sPoints:
			if sPoint:
				sX, sY = sPoint.split(",")
				super().append((float(sX), float(sY)))

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def commit(self):
		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def extend(self, iterable):
		for value in iterable:
			if isinstance(value, list):
				value = tuple(value)
			else:
				assert isinstance(value, tuple)
			assert len(value) >= 2
			super().append(value[:2])

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def append(self, value):
		if isinstance(value, list):
			value = tuple(value)
		else:
			assert isinstance(value, tuple)
		assert len(value) >= 2
		super().append(value[:2])

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def insert(self, index, value):
		if isinstance(value, list):
			value = tuple(value)
		else:
			assert isinstance(value, tuple)
		assert len(value) >= 2
		super().insert(index, value[:2])

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def clear(self):
		super().clear()

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def pop(self, index:int = -1):
		ret = super().pop(index)

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)

		return ret
	#

	def remove(self, value):
		if isinstance(value, list):
			value = tuple(value)
		else:
			assert isinstance(value, tuple)
		assert len(value) >= 2
		super().remove(value[:2])

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)

		return ret
	#

	def reverse(self):
		super().reverse()

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def copy(self):
		return PointsList(self)
	#

	def sort(self, key=None, reverse=False):
		super().sort(key=key, reverse=reverse)

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def __delitem__(self, key):
		ret = super().__delitem__(key)

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)

		return ret
	#

	def __setitem__(self, index, value):
		if isinstance(value, list):
			value = tuple(value)
		else:
			assert isinstance(value, tuple)
		assert len(value) >= 2
		super().__setitem__(index, value[:2])

		if self._connectedSVGControl is not None:
			self._connectedSVGControl.attributes["points"] = str(self)
	#

	def __str__(self):
		return " ".join([
			(str(vx) + "," + str(vy)) for vx, vy in self
		])
	#

#






