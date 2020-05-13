def ejercicio1(a):
    dinero={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    print(dinero.get(a,"No existe"))

def ejercicio2(a,b,c,d):
    diccionario={"Nombre": a,"Edad": b , "Direccion":c,"telefono":d}
    print(diccionario["Nombre"]," tiene ",diccionario["Edad"]," y vive en ",diccionario["Direccion"]," y con telefono ",diccionario["telefono"])

def ejercicio3(b,**a):
    kilos=int(input("Ingrese numero de kilos "))
    if b in a:
        print("Pidio ",kilos," kilos de",b ," con un total de ",a[b]*kilos)
    else:
        print("No existe")
        
def ejercicio4():
    d={1:'enero', 2 :'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    date = input('Introduce una fecha en formato dd/mm/aaaa: ')
    date = date.split('/')
    print(date[0],date[1],date[2])
    print(date[0]," de ",d[int(date[1])]," del ", date[2])

def ejercicio5():
    d={'Matemáticas': 6 , 'Física' : 4 , 'Química' : 5} 
    credito=0
    for i,j in d.items():
        print("Curso: ",i,"Promedio: ",j)
        credito+=j
    print("Promedio Final: ",credito)
    
def ejercicio6():
    directorio={}
    condicion="Si"
    while condicion=="Si":
        valor1=input("INGRESE PALABRA ")
        valor2=input(valor1+": ")
        directorio[valor1]=valor2
        condicion=input("Ingrese si desea seguir agregando ")
    print(directorio)
    
def ejercicio7():
    directorio={}
    condicion="Si"
    while condicion=="Si":
        valor1=input("Ingrese viveres :")
        valor2=input(valor1+":")
        directorio[valor1]=valor2
        condicion=input("Desea seguir agregando Si/No  ")
    print("Lista de compras")
    suma=0
    for i,j in directorio.items():
        print(i,j)
        suma+=float(j)
    print("La suma todal es de " ,suma)
        
def ejercicio8():
    directorio={}
    condicion="Si"
    while condicion=="Si":
        valor1=input("Ingrese palabra y traduccion :")
        valor2=input(valor1+":")
        directorio[valor1]=valor2
        condicion=input("Desea seguir agregando Si/No  ")
    print("Palabras en ingles")
    frase=input()
        
    for i in frase.split():
        if i in directorio:
            print(directorio[i],end="")
        else:
            print(i)

def ejercicio9():
    pagado=0
    deuda=0 
    numero="P"
    directorio={}
    while numero!="T":
        numero=input("¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?")
        if numero=="A":
            print("Usted eligio nueva factura")
            num=input("Ingrese numero de orden: ")
            factura=input(num+": ")
            directorio[num]=factura
            #for i,j in directorio.items():
            #    print(i,j)
            #    deuda+=float(j)
            deuda=int(deuda)+int(factura)
            print("La suma de las deudas es: ",deuda)
            print("Lo que ha pagado",pagado)
        elif numero=="P":
            print(directorio)
            orden=str(input("Ingrese el numero de factura que desea pagar"))
            tmp=0
            
            for i,j in directorio.items():
                if i==orden:
                    tmp=j
            directorio.pop(orden)
            print(directorio)
            pagado=pagado+int(tmp)
            deuda=deuda-int(tmp)
            print("La suma de las deudas es: ",deuda)
            print("Lo que ha pagado",pagado)
        elif numero=="T":
            print("T")
        else:
            print("Introduzca una letra valida")
        
def ejercicio10():
    clients = {}
    option = ''
    while option != '6':
        if option == '1':
            nif = input('Introduce NIF del cliente: ')
            name = input('Introduce el nombre del cliente: ')
            address = input('Introduce la dirección del cliente: ')
            phone = input('Introduce el teléfono del cliente: ')
            email = input('Introduce el correo electrónico del cliente: ')
            vip = input('¿Es un cliente preferente (S/N)? ')
            client = {'nombre':name, 'dirección':address, 'teléfono':phone, 'email':email, 'preferente':vip=='S'}
            clients[nif] = client
        if option == '2':
            nif = input('Introduce NIF del cliente: ')
            if nif in clients:
                del clients[nif]
            else:
                print('No existe el cliente con el nif', nif)
        if option == '3':
            nif = input('Introduce NIF del cliente: ')
            if nif in clients:
                print('NIF:', nif)
                for key, value in clients[nif].items():
                    print(key.title() + ':', value)
            else:
                print('No existe el cliente con el nif', nif)
        if option == '4':
            print('Lista de clientes')
            for key, value in clients.items():
                print(key, value['nombre'])
        if option == '5':
            print('Lista de clientes preferentes')
            for key, value in clients.items():
                if value['preferente']:
                    print(key, value['nombre'])
        option = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')


#ejercicio1("Nuevo sol peruano")
#ejercicio1("Yen")
#ejercicio1("Euro") 
#ejercicio2("Rodrigo",19,"Av.Venezuela",924872395)
#ejercicio3( "Pera",Plátano=1.35, Manzana=0.8, Pera=0.85, Naranja=0.7 )
#ejercicio4()   
#ejercicio5()
#ejercicio6()
#ejercicio7()
#ejercicio8()
#ejercicio9()
ejercicio10()