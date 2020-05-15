import csv
with open('C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\employees.csv') as archivo:
    leer=csv.reader(archivo)
    lista_datos=list(leer)
print(lista_datos)

        
    
