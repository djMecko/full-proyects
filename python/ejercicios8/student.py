from person import Person

class Student(Person):

	def __init__(self, name, age, dni, school):
		super().__init__(name, age, dni)
		self.school = school		

	def get_info(self):
		print("---- informacion ----")
		print("name: " + self.name)
		print("age: " + str(self.age))
		print("dni: " + self.dni)
		print("school: " + self.school)

	def get_age(self):
		return self.age
