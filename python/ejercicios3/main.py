# Ejercicios

# Ejercicio 1 
# input: array1 = [], array2 = []
# output: equal size return true else return false
def equal_size(array1, array2):
	return len(array1) == len(array2);

# Ejercicio 2
# input: array1 = [], array2 = []
# output: return sum of arrays
def sum_arrays(array1, array2):
    suma=[]
    if len(array1) == len(array2):
        for i in range(len(array1)):
            suma.append(array1[i]+array2[i])
    else:
        suma.append("Error: diferente sizes")
    return suma;
            	
# Ejercicio 3
# input: array1 = [], array2 = []
# output: return true if are equals else return false
def are_equals(array1, array2):
    if array1==array2:
        return True;
    else:
        return False;

# Ejercicio 4
# input: array1 = []
# output: return an array duplicate
def duplicate(array1):
    suma=[]
    for i in range(len(array1)):
        suma.append(array1[i]*2)
    return suma;

# Ejercicio 5
# input: array1 = [], array2 = []
# output: return true if an array is the reverse of the other
def is_reverse(array1, array2):
    return;
# Ejercicio 6
# input: array1 = [], number = int
# output: return an array with the number less to n
def less_to(array1, number):
    suma=[]
    for i in range(len(array1)):
        if array1[i]<number:
            suma.append(array1[i])
    return suma;

# Ejercicio 7
# input: array1 = [], find_number = int, replace_number
# output: return an array with the numbers replaced
def replace_number(array1, find_number, replace_number):
    array1[find_number]=replace_number
    return array1;

# Ejercicio 8
# input: array1 = []
# output: return the minimun number of the array
def minimun_number(array1):
	newarray=[]
	for i in range(len(array1)):
        if array1[i]<array1[i+1]:
            newarray
     
     
# Ejercicio 9
# input: array1 = [(a,b)]
# output: return the name of the cheaper fruit
def cheap_fruit(array1):
	most_cheap = ("none",1000);
	for item in array1:
		if item[1] < most_cheap[1]:
			most_cheap = item
	return most_cheap[0];

# Ejercicio 10
# input: array1 = [(a,b)]
# output: return the name of most expensive fruit
def expensive_fruit(array1):
	return ;

print("Ejercicio 1")
print(equal_size([1,2,3],[4,5,6])) # Rpta: true
print(equal_size([1,2,3],[4,5])) # Rpta: false
print("Ejercicio 2")
print(sum_arrays([1,2,3],[4,5,6])) # Rpta: [5, 7, 9]
print(sum_arrays([1,2,3],[4,5])) # Rpta: Error: diferente sizes
print("Ejercicio 3")
print(are_equals([1,2,3], [1,2,3])) #Rpta: true
print(are_equals([1,2,3], [1,1,3])) #Rpta: false
print("Ejercicio 4")
print(duplicate([1,2,3])) #Rpta: [2, 4, 6]
print("Ejercicio 5")
print(is_reverse([1,2,3], [3,2,1])) # Rpta: true
print(is_reverse([1,2,3], [2,2,1])) # Rpta: false
print("Ejercicio 6")
print(less_to([1,4,6,8,3],5)) # Rpta: [1, 4, 3]
print("Ejercicio 7")
print(replace_number([1,4,6,8,4],4, 9)) # Rpta: [1, 9, 6, 8, 9]
print("Ejercicio 8")
print(minimun_number([6,53,2,6])) # Rpta: 2
print("Ejercicio 9")
print(cheap_fruit([("manzana", 10), ("pera", 2), ("uva", 5)])) # Rpta: "pera"
print("Ejercicio 10")
print(expensive_fruit([("manzana", 10), ("pera", 2), ("uva", 5)])) # Rpta: "manzana"
