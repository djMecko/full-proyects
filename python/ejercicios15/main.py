def ejercicio1(*cursos):
    for cursos in cursos:
        print(cursos)

def ejercicio2(*cursos):
    print("Yo estudio", end=" ")
    for cursos in cursos:
        print(cursos, end=" ,")

def ejercicio3(*cursos):
    notas = []
    for j in range(len(cursos)):
        print(cursos[j])
        notas.append(input("Ingrese nota: "))
    
    for i in range(len(cursos)):
        print("Curso: ",cursos[i],"  Notas: ",notas[i])


def ejercicio4(*v):
    UNO = [0,94,14,12,10,2,0]
    UNO.sort()

    print("Los números ganadores son " + str(UNO))
        
def ejercicio5(*numero):
    for i in range(len(numero)-1,-1,-1):
        print(numero[i])

def ejercicio6(*curso):
    cursos=[]
    nota=[]
    for i in range(len(curso)):
        print(curso[i])
        number=int(input("Ingrese su nota"))
        if number<12:
            nota.append(number)
            cursos.append(curso[i])
    print(nota)
    print(cursos)

def ejercicio7(letra):
    for i in range(len(letra),1,-1):
        if i%3==0:
            letra.pop(i-1)
    print(letra)

def ejercicio8(palabra1,palabra2):
    new=[]
    var=0
    for i in range(len(palabra2)):
        new.append(palabra2[i])
    new.reverse()
    if palabra1==new:
        print("Son palindromos")
    else:
        print("No son palindromos")
        
        
def ejercicio9(palabra):
    vocals = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocals: 
        veces = 0
        for letra in palabra: 
            if letra == vocal:
                veces += 1
        print("La vocal " + vocal + " aparece " + str(veces) + " veces")
        
def ejercicio10(array):
	for i in range(0, len(array)):
    		for j in range(0, len(array)):
			    if array[i] < array[j]:
				    tmp = array[i]
				    array[i] = array[j]
				    array[j] = tmp;
	print(array)

def ejercicio11(a,b):
    multi=[]
    suma=0
    final=0
    for i in range(len(a)):
        final+=a[i]*b[i]
    print(final)


    
 

#ejercicio1("matematica","quimica","fisica","historia","lengua")
#ejercicio2("matematica","quimica","fisica","historia","lengua")
#ejercicio3("matematica","quimica","fisica","historia","lengua")
ejercicio4(0,94,14,12,10,2,0)
#ejercicio5(1,2,3,4,5,6,7,8,9,10)
#ejercicio6("matematica","quimica","fisica","historia","lengua")
#ejercicio7(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
#ejercicio8("aarañara","araañara")
#ejercicio9("aaaeei")
#ejercicio10([50, 75, 46, 22, 80, 65, 8])
#ejercicio11((1,2,3),(-1,0,2))

