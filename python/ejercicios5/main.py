# Insertion sort
# https://visualgo.net/bn/sorting

def inser_sort(array):
	for i in range(0, len(array)):
		for j in range(0, len(array)):
			if array[i] < array[j]:
				tmp = array[i]
				array[i] = array[j]
				array[j] = tmp;
	return array

print(inser_sort([45,33,1,22]))
