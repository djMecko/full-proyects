class Person:

	# constructor de la clase
	def __init__(self, name, age, dni):
		self.name = name
		self.age = age
		self.dni = dni

	def get_info(self):
		print("name: " + self.name)
		print("age: " + str(self.age))
		print("dni: " + self.dni)
