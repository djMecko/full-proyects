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

# Revisar

# https://www.w3schools.com/python/python_classes.asp
# https://www.learnpython.org/en/Classes_and_Objects


# Clase Felino
# Clase paquidermo
# Clase pescado


class Felino:
    def __init__(self,nombre,edad,sano,raza):
        self.nombre= nombre
        self.edad = edad
        self.sano = sano
        self.raza = raza
        self.especie = "Felino"
    
    def sacando_info(self):
        print("----Datos del Mishifus----")
        print("name:\t"+str(self.nombre))
        print("edad:\t"+str(self.edad))
        print("salud:\t"+str(self.sano))
        if self.sano == True:
            print("El gato esta bien")
        else:
            print("El gato esta mal")
        print("raza:\t"+str(self.raza))
        print("especie:\t"+str(self.especie))
        print("---------FIN-----------")
    
        
felino = Felino("Juanito",15,False,"Mestiso")
print(felino.sacando_info())


#Clase Paquidermo

class Paquidermo:
    def __init__(self,nombre,edad,sano,raza,tamano,peso):
        self.nombre= nombre
        self.edad = edad
        self.sano = sano
        self.raza = raza
        self.tamano = tamano
        self.peso = peso
        self.especie = "Hipopotamo"
    
    def sacando_info(self):
        print("----Datos del Gordo :v----")
        print("name:\t"+str(self.nombre))
        print("edad:\t"+str(self.edad))
        print("salud:\t"+str(self.sano))
        if self.sano == True:
            print("El Hipopotamo esta bien")
        else:
            print("El Hipopotamo esta mal")
        print("raza:\t"+str(self.raza))
        print("tamaño:\t"+str(self.tamano))
        print("peso:\t"+str(self.peso))
        print("especie:\t"+str(self.especie))
        print("---------FIN-----------")
    
        
paquidermo = Paquidermo("Gloria",12,True,"Choeropsis",1.92,"900 kg")
print(paquidermo.sacando_info())

#Clase Pescado

class Pescado:
    def __init__(self,peso,tamano,tipo,parte):
        self.peso = peso
        self.tamano = tamano
        self.tipo = tipo
        self.parte = parte
    
    def sacando_info(self):
        print("---Datos del Nemo----")
        print("Peso: "+str(self.peso))
        print("Tamano: "+str(self.tamano))
        print("Tipo: "+str(self.tipo))
        print("Parte: "+str(self.parte))

pescado = Pescado("4kg","10cm","Furel","Pierna")
print(pescado.sacando_info())