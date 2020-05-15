n=int(input("INTRODUSCA EL NUEVO NOMRBRE DE LA TABLA"))
nombre= 'tabla del ' +str(n) + 'ejercicio1.txt'
try:
    nombre=open(nombre,'r')
except FileNotFoundError:
    print("No existe el fichero antes mencionaod")
else:
    print(nombre.read())
