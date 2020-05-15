import csv
csv.register_dialect('dialecto_csv',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL
                     )


with open('C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\temp.csv') as archivo:
    print("Eliminando simbolos y comillas")
    file = csv.reader(archivo,dialect='dialecto_csv')
    for row in file:
        print(', '.join(row))
        