import csv
data = csv.DictReader(open("C:\\Users\\rRodrigo\\Desktop\\full-proyects\\python\\CSV\\departments.csv"))
print("CSV file as a dictionary:\n")
for row in data:
    print(row)
