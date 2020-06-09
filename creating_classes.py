class Car:
	"""
	Docstring describing the class
	"""

	def __init__(self, engine, tires):
		"""
		Docstring describing the method
		"""
		self.engine = engine
		self.tires = tires
		
	def description(self):
		print(f"A car with an {self.engine} engine, and {self.tires}")

	def wheel_circumference(self):
		if len(self.tires) > 0:
			return self.tires[0].circumference()
		else:
			return 0