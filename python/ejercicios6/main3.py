# Vamos a hacer que una funcion pueda reconocer el tipo
# de objeto que ingresa y retorna un resultado segun el tipo 
# de objeto

# Para esto crearemos una funcion que suma un entero con cualquier cosa
# entonces yo defino que operacion realizara
def int_sum(number, other):
	if isinstance(other, int): # Suma con otro entero y retorna un entero
		return number + other
	elif isinstance(other, list): # Suma con una lista y retorna una lista
		newArray = []
		for i in range(0, len(other)):
			newArray.append(number + other[i]  )
		return newArray
	elif isinstance(other, basestring): # suma con un string y retorna un string
		return str(number) + other 

# Es una suma normal
print(int_sum(1, 1)) # Rpta:  1
# Agrega 1 a cada elemento de la lista
print(int_sum(1, [2, 3, 4, 5])) # Rpta: [3, 4, 5, 6] 
# Yo lo defino como concatenar un numero al inicio de un string
print(int_sum(1, "hola")) # Rpta: "1hola"
