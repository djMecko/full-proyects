# Revisar algoritmos de ordenacion

# insert sort
# https://visualgo.net/bn/sorting
# quick sort
# https://www.geeksforgeeks.org/quick-sort/

# recursividad

# Ejercicio: Factorial
# factorial(3) = 3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(1) = 1

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n -1)

print("Ejercicio 1")
# 3 * factorial( 2)
# 3 * 2 * factorial (1)
# 3 * 2 * 1
print(factorial(3))
# 5 * factorial (4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
print(factorial(5))

# Ejercicio 2: Potencia
# potencia(3,5) = 3*3*3*3*3
# potencia(2,3) = 2*2*2
# potencia(1,5) = 1*1*1*1*1
def potencia(n, exp):
	if exp == 1:
		return n
	else:
		return n * potencia(n, exp - 1)

print(potencia(3,5))
# 3 * potencia(3, 4)
# 3 * 3 * potencia(3, 3)
# 3 * 3 * 3 * potencia(3, 2)
# 3 * 3 * 3 * 3 * potencia(3, 1)
# 3 * 3 * 3 * 3 * 3 
# = 243

# Ejercicio 3: Contar digitos
# count_digits(123) = 1 + 1 + 1
# count_digits(1235) = 1 + 1 + 1 + 1

def count_digits(n):
	if n < 10:
		return 1
	else:
		return 1 + count_digits(n/10)
print(count_digits(123))
# 1 + count_digits(12)
# 1 + 1 + count_digits(1)
# 1 + 1 + 1
# = 3









