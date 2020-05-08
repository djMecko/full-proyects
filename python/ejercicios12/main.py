def Ejercicio1():
    return print("¡HOLA MUNDO!")
    
def Ejercicio2():
    var = "¡HOLA MUNDO!"
    return print(var)

def Ejercicio3():
    print("ingrese su nombre")
    nombre = str(input())
    print("¡¡¡Hola "+ nombre + "!!!")
    
def Ejercicio4():
    print("Ingrese su nombre")
    nombre = str(input())
    print("Ingrese numero de repeticiones")
    repetir = int(input())
    for i in range(repetir):
        print(nombre)

def Ejercicio5():
    print("Ingrese su nombre")
    nombre = str(input())
    n = len(nombre)
    print(nombre.upper())

def Ejercicio6():
    aritmetica = ((3+2)/(2*5))**2
    print(aritmetica)

def Ejercicio7():
    print("Ingrese horas trabajadas")
    h = int(input())
    print("Ingrese pago por hora")
    c = int(input())
    print("Su paga es: "+str(h*c))

def Ejercicio8():
    print("Ingrese nùmero")
    n = int(input())
    print("La suma de 1 hasta "+str(n)+" es: " + str(int((n*(n+1)/2))))

def Ejercicio9():
    p = float(input("Cual es su peso en KG: "))
    a = float(input("Cual es tu altura: "))
    print("Su indice de masa corporal es: ",float(p/(a**2)))
    
def Ejercicio10():
    n1 = int(input("Ingresa el dividendo"))
    n2 = int(input("Ingresa un divisor"))
    print(str(n1) + "entre" + str(n2)+"me da un cociente de: "+str(n1/n2) + " y un residuo de: "+ str(n1%n2) )
    
def Ejercicio11():
    n1 = float(input("Cantidad a invertir"))
    n2 = float(input("Interes anual"))
    n3 = int(input("Cantidad de años"))
    print("Respuesta: ", n1*(n2/100)**n3)

def Ejercicio12():
    peso_payaso = 112
    peso_munecas = 75
    payaso = int(input("Ingrese numero de payasos vendidos: "))
    munecas = int(input("Ingrese numero de muñecas vendidas: "))
    print("El peso total es de: " , peso_munecas*munecas+peso_payaso*payaso)

def Ejercicio13():
    monto=float(input("Ingrese monto de dinero: "))
    interes = 0.04
    primer_interes = monto*interes
    primer_mes = monto + primer_interes
    print("1: ",primer_mes)
    segundo_interes = primer_mes*interes
    segundo_mes = primer_mes + segundo_interes
    print("1: " ,round(segundo_mes,2))
    tercer_interes = segundo_mes * interes
    tercer_mes = segundo_mes + tercer_interes
    print("1: " ,round(tercer_mes,2))


def Ejercicio14():
    barras = int(input("Ingrese BAR "))
    precio = 3.49
    descuento = 0.6
    coste = (barras*precio)*descuento
    print("Pan fresca: " + str(precio))
    print("el descuento del pan es " + str(descuento * 100))
    print("El coste final a pagar es " + str(round(coste,2)))

#Ejercicio1()
#Ejercicio2()
#Ejercicio3()
#Ejercicio4()
#Ejercicio5()
#Ejercicio6()
#Ejercicio7()
#Ejercicio8()
#Ejercicio9()
#Ejercicio10()
#Ejercicio11()
#Ejercicio12()
Ejercicio13()
#Ejercicio14()