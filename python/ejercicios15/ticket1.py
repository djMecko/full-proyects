def problema1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("+",end="")
        print("")
        
def problema2(n):
    suma=0
    for i in range(1,n+1):
        suma+=1
        for j in range(1,n+1):
           if suma==j:
               print("O",end="")
           else:
               print("X",end="")
        print("")

problema1(4)
problema2(4)

