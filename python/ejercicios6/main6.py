# Clases abstractas

import abc
from abc import ABC

class Animal(ABC):
 	
 	# Create constructor not working
	# def __init__(self,name):
	#	self.name = name

	@abc.abstractmethod 
	def setName(self, name):
		pass

	@abc.abstractmethod
	def getName(self):
		pass

# Instanciate an abstract class not working
# animal = Animal()

class Perro(Animal):
    
    def __init__(self):
      	pass  

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name

perro = Perro()
perro.setName("Marly")
print(perro.getName())

# python3 main6.py 
# http://www.pythondiario.com/2018/08/clases-abstractas-ejemplos-practicos.html
