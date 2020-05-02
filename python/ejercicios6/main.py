# Programacion orientada a objetos
# Atributos: publicos y privados
class Dog:

	def __init__(self, name, color, year, healthy):
		self.name = name
		self.color = color
		self.__year = year
		self.kind = "canino"
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

fido = Dog("Fido", "plomo", 2018, True)
fido.get_info()
fido.set_comments("Este perro se encuentra en buen estado")
print(fido.comments)

toribio = Dog("toribio", "negro", 2016, True)
fido.get_info()

# Clase Felino
# Clase paquidermo
# Clase pescado
