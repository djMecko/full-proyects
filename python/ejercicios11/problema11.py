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
    
class Curso(Estudiante):
    def __init__(self,nombre,edad,materia):
        super().__init__(nombre,edad)
        self.materia = materia
    def get_info(self):
        
        return "Lista 1"

        

def menu():
    print("Seleccione un opciòn del 1 al 3")
    print("1: Agregar estudiante")
    print("2: Ver estudiantes")
    print("3: Salir del programa")
    
    seleccion= int(input())
    if seleccion == 1:
        print("Ingrese su nombre")
        name = str(input())
        print("Ingrese su edad")
        age = str(input())
        print("Ingrese su curso")        
        course = str(input())
        curso = Curso(name,age,course)
        return menu()
    elif seleccion == 2:
        print("Ver la lista de alumnos")
        Curso.get_info()

        return menu()
    elif seleccion == 3:
        print("Saliendo del programa...Bye")
    else:
        print("Elije del 1 al 3")

    
print(menu())