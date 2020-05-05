from person import Person

class Teacher(Person):

	def __init__(self, name, age, dni, school):
		super().__init__(name, age, dni)
		self.school = school		

	def get_info(self):
		print("name: " + self.name)
		print("age: " + str(self.age))
		print("dni: " + self.dni)
		print("school: " + self.school)
