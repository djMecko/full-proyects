import csv
columnas=[]
with open('C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\departments.csv') as f:
    archivo=csv.reader(f,delimiter=" ",quotechar=",")
    columnas=next(archivo)
    for row in archivo:
        print(', '.join(row))
    
print(columnas)
print("El total de lineas de filas es: " ,archivo.line_num)
print("Y el total de campos es:")
print(", ".join(columnas))

