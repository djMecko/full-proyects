import csv
with open('C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\countries.csv') as archivo:
    paises=csv.reader(archivo)
    for row in paises:
        print(','.join(row))
        