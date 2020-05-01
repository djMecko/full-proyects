import math

# Ejercicios 1: Escribir un ejemplo con cada funcion de la libreria math y entenderla
# Si tiene conceptos matematicos desconocidos, solo hacer el ejemplo y pasar al siguiente
# Documentation: https://docs.python.org/3/library/math.html

print(math.ceil(10.11))	# Rpta: 11
# print(math.comb(10, 4)) # Error not working
print(math.fabs(-7.7))	#Rpta: 7.7
print(math.factorial(4)) #devuelve el factorial de un numero
print(math.copysign(-100,40 ) ) #Devuelve el factorial del primero???
print(math.fabs( -19)) #Rpta 19 devuelve el valor absoluto


# Ejercicios 2: Escribir un ejemplo para cada funcion de string
# Documentation: https://docs.python.org/2.5/lib/string-methods.html
texto_prueba = "RoDriGo"
print(texto_prueba.capitalize())
print(texto_prueba.center(20, '-'))
print(texto_prueba.lower())
print(texto_prueba.upper())
print(texto_prueba.expandtabs(3) )