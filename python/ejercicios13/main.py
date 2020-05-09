def problema1(edad):
    if edad < 18:
        print("Es menor")
    else:
        print("Es mayor")
    
def problema2(clave,password):
    #clave=str(input("Inserte su contraseña"))
    #password =str(input("Escriba la contraseña para verificar"))
    if clave==password:
        print("Coincide")
    else:
        print("No coincide")
        
def problema3(num1,num2):
    print("Su divisor es: ",num1)
    print("Su dividendo es ",num2)
    if num1 != 0:
        print(num2/num1)
    else:
        print("Ingrese un numero diferente")

def problema4(num):
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def problema5(edad,ingreso):
    if edad>16 and ingreso>=1000:
        print("Puedes tributar")
    else:
        print("No puedes tributar")
        
def problema6(nombre,sexo):
    if (sexo == "m" and nombre < 'm') or (sexo=="h" and nombre < 'n'):
        print("GRUPO A")
    else:
        print("GRUPO B")
        
def problema7(dinero):
    if dinero<10000:
        print("5%")
    elif dinero<20000:
        print("15%")
    elif dinero<35000:
        print("20%")
    elif dinero<60000:
        print("30%")
    else:
        print("45%")

def problema8(bonificacion):
    dinero = 2400
    extra = bonificacion*2400
    if bonificacion<0.4:
        print("inaceptable")
    elif bonificacion<0.6:
        print("Aceptable ", extra)
    else:
        print("Meritorio ",extra)
        
def problema9(edad):
    if edad < 4:
        print("Entras gratis")
    elif edad < 18:
        print("Pagas s/5")
    else:
        print("Pagas s/10")
        
def problema10(*arg):
    print("Que ingrediente deseas: pimiento y tofu,  peperoni, jamon y salmon.")
    resultado = ""
    for i in range(len(arg)):
        if arg[i] == "pimiento" or arg[i]=="tofu":
            resultado= "Vegetariana"
        else:
            resultado= "No es Vegetariana" 
    print(resultado)
    for i in range(len(arg)):
        print(arg[i])
        
#problema1(19) #Es mayor
#problema1(13) # es menor
#problema2("rodrigo", "rodrigo") #coincide
#problema2("rodrigo", "Juan") #No coincide
#problema3(0,10) #erro
#problema3(10,20) #2
#problema4(11) #Es impar
#problema4(2) #Es par
#problema5(17,1200)
#problema5(14,1200)
#problema6("rodrigo", "h")
#problema6("amelia", "m")
#problema7(1000)
#problema7(100000000)
#problema8(0.6)  #Meritorio 1440
#problema8(0.1)  #Inaceptable
#problema9(10) #Pagas 5
#problema9(2)  #entras gratis
#problema9(22)  #Pagas 10
problema10("pimiento","salmon","peperoni")
problema10("tofu","pimiento")
