class Wheel:
	
	def __init__(self, color, size):
		self.color = color
		self.size = size

	def get_velocity(self):
		return self.size * 10

class Auto:

	def __init__(self, numberWheels, sizeWheel):
		self.numberWheels = numberWheels
		self.wheel = Wheel("black", sizeWheel)

	def get_auto_velocity(self):
		return self.wheel.get_velocity() * self.numberWheels;


#auto = Auto(4, 10)
#print(auto.get_auto_velocity())

class Figure:

	def __init__(self, color, name):
		self.color = color
		self.name = name

	def get_color(self):
		return self.color

	def get_name(self):
		return self.name

	def get_area(self):
		return 0

class Square(Figure):

	def __init__(self, color, name, sides):
		Figure.__init__(self, color,  name)
		self.sides = sides

	def get_sides(self):
		return sides

	def get_area(self):
		return self.sides * 10

class Triangle(Figure):

	def __init__(self, color, name, sides):
		Figure.__init__(self, color,  name)
		self.sides = sides

	def get_sides(self):
		return sides

	def get_area(self):
		return self.sides * 5


cuadrado = Square("red", "cuadrado", 4)
print(cuadrado.get_area())

triangulo = Triangle("red", "cuadrado", 4)
print(triangulo.get_area())