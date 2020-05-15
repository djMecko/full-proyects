import csv
with open('C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\departments.csv') as file:
    archivo=csv.reader(file, delimiter=' ', quotechar='|')
    for row in archivo:
        print(','.join(row))
        
        
    