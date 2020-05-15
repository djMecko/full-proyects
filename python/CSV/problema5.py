import csv
with open('C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\departments1.csv') as archivo:
    print("Eliminando los espacios al inicio del texto")
    lista =  csv.reader(archivo,skipinitialspace=True) #Skipinitialspace, elimina los espacios si es que hay al inicio del texto o de las frases en comas
    for row in lista:
        print(', '.join(row))
        
with open('C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\departments1.csv') as archivo:
    print("Sin eliminar los especios en los textos")
    lista =  csv.reader(archivo,skipinitialspace=False) #Skipinitialspace, elimina los espacios si es que hay al inicio del texto o de las frases en comas
    for row in lista:
        print(', '.join(row))
        