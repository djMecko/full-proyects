
def sum_int(variable1, variable2):
	newArray = []
	if isinstance(variable2, int) and isinstance(variable1, int):
		return variable1 + variable2
	elif isinstance(variable1, int) and isinstance(variable2, list):
		for item in variable2:
			newArray.append(variable1 + item)
		return newArray
	elif isinstance(variable1, list) and isinstance(variable2, int):
		for item in variable1:
			newArray.append(item + variable2)
		return newArray
	elif isinstance(variable1, list) and isinstance(variable2, list):
		for i in range(0, len(variable1)):
			newArray.append(variable1[i] + variable2[i])
		return newArray

#print(sum_int(1, 1))
#print(sum_int(1, [2,3,4]))
#print(sum_int([2,3,4], 1))
#print(sum_int([2,3,4], [2,3,5]))

class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_info(self):
		print(self.name)

#perro = Dog("fido")

dogs = []

for i in range(0,10):
	dogs.append(Dog("fido" + str(i), i))

for item in dogs:
	print(item.name + " edad: " + str(item.age))

