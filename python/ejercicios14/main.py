def ejercicio1(palabra):
    for i in range(10):
        print(palabra)

def ejercicio2(edad):
    for i in range(edad):
        print("Edad: ", i+1)
        
def ejercicio3(numero):
    for i in range(numero):
        if i%2!=0:
            print(str(i),end=",")

def ejercicio4(numero):
    for i in range(numero,-1,-1):
        print(i)
        
def ejercicio5(dinero,interes,year):

    for i in range(year):
        dinero = dinero * (1 + 10/100)
        #dinero= dinero+(dinero*(interes/100))
        print("dinero: ",dinero,"  Interes: ",interes)

def ejercicio6(entero):
    for i in range(entero):
        print("*"*(i+1))

def ejercicio7():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j,end="\t")
        print("")
        
def ejercicio8(n):
    for i in range(1,n+1,2):
        for j in range(i,0,-2):
            print(j, end="")
        print("")
        
def ejercicio9(contrasena):
    entrada= str(input("identificate"))
    if contrasena == entrada:
        print("Clave correcta")
    else:
        return ejercicio9(contrasena)

def ejercicio10(n):
    var=0
    for i in range(2,n+1):
        if n % i == 0:
            var+=1
    if var>1:
        print("No es primo")
    else:
        print("Es primo")
def ejercicio11(n):
    for i in range(len(n)-1,-1,-1):
        print(n[i])

def ejercicio12(palabra,letra ):
    var=0
    for i in range(len(palabra)):
        if palabra[i] == letra:
            var+=1

        print(palabra[i])
    print("En la palabra: ",palabra," se repitio las letras:",letra, "unas:",var,"veces")
    
def ejercicio13():
    texto = str(input("INgrese palabra "))
    if texto != "adios":
        print(texto)
        return ejercicio13()
    
    
#ejercicio1("Rodrigo")
#ejercicio2(40)s
#ejercicio3(10)
#ejercicio4(9)
#ejercicio5(1000,10,5)
#ejercicio6(5)
#ejercicio7()
#ejercicio8(9)
#ejercicio9("1234")
#ejercicio10(97)
#ejercicio11("HOLA")
#ejercicio12("Cachetada","a")
ejercicio13()
