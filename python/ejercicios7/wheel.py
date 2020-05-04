class Wheel:
	
	def __init__(self, color, size):
		self.color = color
		self.size = size

	def get_velocity(self):
		return self.size * 10
