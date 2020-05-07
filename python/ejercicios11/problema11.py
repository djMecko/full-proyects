"""solo que tienes q usar la clase estudiante
    y tambien la clase curso
    en el menu ahora es asi
    1 Ingresar estudiante
    2 Lista estudiantes
    3 Agregar  curso
    4 Listar cursos"""

class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def get_info(self):
        print("nombre:" + self.nombre)
        print("edad  :" + str(self.edad))


class Curso:
    def __init__(self,materia):
        self.materia = materia

    def get_info(self):
        print("curso  :" + str(self.materia))

estudiantes = []
cursos = []

def menu():
    print("Seleccione un opcion del 1 al 3")
    print("1: Agregar estudiante")
    print("2: Ver estudiantes")
    print("3: Agregar curso")
    print("4: Ver cursos")
    print("5: Salir del programa")
    
    seleccion= int(input())
    if seleccion == 1:
        name = str(input("Ingresar nombre: "))
        age = str(input("Ingresar edad: "))
        estudiantes.append(Estudiante(name, age))
        return menu()
    elif seleccion == 2:
        print("Ver la lista de alumnos")
        for item in estudiantes:
            item.get_info()
        return menu()
    if seleccion == 3:
        materia = str(input("Ingresar materia: "))
        cursos.append(Curso(materia))
        return menu()
    elif seleccion == 4:
        print("Ver la lista de cursos")
        for item in cursos:
            item.get_info()
        return menu()
    elif seleccion == 5:
        print("Saliendo del programa...Bye")
    else:
        print("Elije del 1 al 3")

menu()