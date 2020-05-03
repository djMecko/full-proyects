class myList:

	def __init__(self, array):
		self.array = array

	def show(self):
		print(self.array)

	def max(self):
		maximun = self.array[0]
		for element in self.array:
			if maximun < element:
				maximun = element
		return maximun

	def min(self):
		pass

	def multiply(self, number):
		newArray = []
		for element in self.array:
			newArray.append(element*number)
		return newArray

	def multiply2(self, number):
		newArray = []
		for element in self.array:
			newArray.append(element*number)
		return myList(newArray)

	def sum(self, other):
		if isinstance(other, int):
			newArray = []
			for i in range(0, len(self.array)):
				newArray.append(self.array[i] + other)
			return newArray
		elif isinstance(other, list):
			newArray = []
			for i in range(0, len(self.array)):
				newArray.append(self.array[i] + other[i])
			return newArray
		elif isinstance(other, myList):
			newArray = []
			for i in range(0, len(self.array)):
				newArray.append(self.array[i] + other.array[i])
			return newArray
		else:
			print("Error: Type no supported")

	def rest(self, other):
		pass

	def mult(self, other):
		pass


milist = myList([1,2,3])
milist2 = myList([2,4,6])

print(milist.sum(1))
print(milist.sum([2,3,4]))
print(milist.sum(milist2))
