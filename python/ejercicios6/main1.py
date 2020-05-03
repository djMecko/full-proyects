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
		print("edad:\t" + str(self.__age()))

	def get_healthy(self):
		return self.__healthy

	def set_healthy(self, healthy):
		self.__healthy = healthy

	def __age(self):
		return 2020 - self.__year

	def set_comments(self, comments):
		self.comments = comments

	def get_random_value(self):
		return "radom_11"
#animal = Animal("fido", "red", 2015, True)
#animal.get_info()

class Paquidermo(Animal):
	pass

#perry = Paquidermo("perry", "green", 2012, True)
#perry.get_info()

class Dog(Animal):
	
	def __init__(self, name, color, year, healthy, legs):
		Animal.__init__(self, name, color, year, healthy)
		self.legs = legs
		self.kind = "Dog"

	def __age(self):
		return (2020 - self._Animal__year)/2

	def get_random_value(self):
		return "radom_22"

 	def get_info(self):
		print("--- Informacion ---")
		print("name:\t" + self.name)
		print("color:\t" + self.color)
		print("tipo:\t" + self.kind)
		# print("edad:\t" + str(self._Animal__age()))
		print("edad:\t" + str(self.__age()))
		print("patas:\t" + str(self.legs))

fido = Dog("fido", "red", 2015, True, 4)
fido.get_info()
print(fido.get_random_value())


class Fish(Animal):
	pass

class Bird(Animal):
	pass
