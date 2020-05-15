def ejercicio1():
    print("¡Hola amiga!")
    return

def ejercicio2(nombre):
    print("¡Hola ",nombre,"!")
    return

def ejercicio3(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)   

def ejercicio4(p,iva=21):
    print("El pago original es: ",p," %")
    print("El impuesto IVA es de: ",iva," %")
    print("Usted debe pagar s/",p+(p*(iva/100)))

def circulo(radio):

    pi = 3.1415
    return 2*pi*radio**2

def cilindro(radio, alto):

    print(circulo(radio)*alto)
    
def ejercicio6(*v):
    suma=0
    for i in range(len(v)):
        suma=suma+v[i]
    media=suma/len(v)
    print(media)
    
def ejercicio7(v):
    cuadrado=[]
    for i in range(len(v)):
        print(v[i])
        cuadrado.append(v[i]**2)
    print(cuadrado)
    
def uno(*sample):

    lista = []
    for i in sample:
        lista.append(i**2)
    return lista

def diccionario(*sample):

    final = {}
    final['media'] = sum(sample)/len(sample)
    final['varianza'] = sum(uno(*sample))/len(sample)-final['media']**2
    final['desviacion tipica'] = final['varianza']**0.5
    print(final)
    
    
def mcd(n1, n2):
    rest = 0
    while(n2 > 0):
        rest = n2
        n2 = n1 % n2
        n1 = rest
    print(n1)
def mcm(n1, n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while (greater % n1 != 0) or (greater % n2 != 0):
        greater += 1
    print(greater)
    
def decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def binario(n):
    lista_binario = []
    while n > 0:
        lista_binario.append(str(n % 2))
        n //= 2
    lista_binario.reverse()
    return ''.join(lista_binario)


#ejercicio1()
#ejercicio2("Rodrigo")
#ejercicio3(4)
#ejercicio4(1000)
#ejercicio4(1000,10)
#cilindro(3,5)
#ejercicio6(1, 2, 3, 4, 5)
#ejercicio6(2.3, 5.7, 6.8, 9.7, 12.1, 15.6)
#ejercicio7([1, 2, 3, 4, 5])
#diccionario(1,2,3,4,5)
#mcd(24,36)
#mcm(24,36)
print(decimal('101101'))
print(binario(23))
