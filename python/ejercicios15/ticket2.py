def ejercicio1(n):
    suma=n+2
    for i in range(1,n+1):
        suma-=1
        for j in range(1,n+1):
            if j<suma:
                print("O",end="")
            else:
                print("X",end="")
        print("")
    
def ejercicio2(n):
    suma=1
    for i in range(1,n+1):
        suma+=1
        for j in range(1,n+1):
            if j<suma:
                print("O",end="")
            else:
                print("X",end="")
        print("")
       
def ejercicio3(n):
    suma=n+1
    for i in range(1,n+1):
        suma-=1
        for j in range(1,n+1):
            if suma<=j:
                print("O",end="")
            else:
                print("X",end="")
        print("")
        
        
def ejercicio4(n):
    suma=0
    for i in range(1,n+1):
        suma+=1
        for j in range(1,n+1):
            if suma<=j:
                print("O",end="")
            else:
                print("X",end="")
        print("")

#ejercicio1(3)
#ejercicio2(3)
#ejercicio3(3)
ejercicio4(3)