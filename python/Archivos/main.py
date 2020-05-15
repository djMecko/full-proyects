n=int(input("Escribe un numero: "))
nombre= 'tabla del ' +str(n) + 'ejercicio1.txt'
archivo=open(nombre,'w')
for i in range(1,11):
    archivo.write(str(n)+" x "+ str(i)+" = "+str(n*i)+"\n")
archivo.close()
