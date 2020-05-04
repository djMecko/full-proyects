# Polimorfismo

class gato():
	def hablar(self):
		print("MIAU")	

class perro():
	def hablar(self):
		print("GUAU")	

class pato():
	def hablar(self):
		print("Quak")	

def escucharMascota(animal):
	animal.hablar()	

if __name__ == '__main__':
	g = gato()
	p = perro()
	d = pato()
	escucharMascota(g)
	escucharMascota(p)
	escucharMascota(d)