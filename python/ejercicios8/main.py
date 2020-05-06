from teacher import Teacher
from student import Student
import random


if __name__ == '__main__':

	maxito = Student("max", 22, "13123","LP")
	rodrigo = Student("rodrigo", 22, "13123","LP")


	arrayStudents = []
	for i in range(0,9):
		student = Student("Nombre"+str(i), random.randint(10, 22), "123123","LP")
		arrayStudents.append(student)
		print(student,i)

	# [Student(), Student(), Student() ... 10]

	for i in range(0,9):
		print(arrayStudents[i].get_age())