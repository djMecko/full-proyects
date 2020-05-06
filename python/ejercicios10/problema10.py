array_nombre=[]
array_edad=[]
def menu():
    print("Seleccione un opciòn del 1 al 3")
    print("1: Agregar estudiante")
    print("2: Ver estudiantes")
    print("3: Salir del programa")

    seleccion=int(input())
    

    if seleccion == 1:
        print("Ingresa el nombre")
        name=str(input())
        print("Ingresa la edad")
        age=str(input())
        array_nombre.append(name)
        array_edad.append(age)
        return menu()

    elif seleccion == 2:
        print("Imprimiendo Lista de estudiantes")
        for i in range(len(array_nombre)):
            print(i+1,"Nombre: ",array_nombre[i]," Edad: ", array_edad[i],"\n")
            return menu()
    elif seleccion == 3:
        print("Usted esta saliendo del programa...adios")
    
    else:
        print("No seas mamon , te dijimos del uno al 3")
    
        
menu()    