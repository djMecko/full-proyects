class Animal:

	def __init__(self, name, color, year, healthy):
		self.name = name
		self.color = color
		self.__year = year
		self.kind = "Animal"
		self.__healthy = healthy

 	def get_info(self):
		print("--- Informacion ---")
		print("name:\t" + str(self.name))
		print("color:\t" + str(self.color))
		print("tipo:\t" + str(self.kind))

	def get_healthy(self):
		return self.__healthy

	def set_healthy(self, healthy):
		self.__healthy = healthy