class Dictionary:
    palabras = []
    significados = []
    def __init__(self,palabra,significado):
        self.palabra = palabra
        self.significado = significado
    
    def add_word(self):
        Dictionary.palabras.append(self.palabra)
        Dictionary.significados.append(self.significado)
    def search_word(self):
        print(Dictionary.palabras)
        print(Dictionary.significados)

        
def menu():
    print("Que desea hacer: ")
    print("1:Añadir palabras: ")
    print("2:Buscar palabras: ")
    print("Para salir presione cualquier boton menos uno y dos")
    dictionary = Dictionary("","") 

    seleccion = int(input())
    if seleccion == 1:
        print("Añadir palabra")
        a= str(input())
        print("Añadir significado")
        b= str(input())
        dictionary = Dictionary(a,b) 
        
        print("Su palabra ha sido agregada exitosamente")
        dictionary.add_word()
        return menu()
        
    elif seleccion == 2:
        dictionary.search_word()
        print("Busque su palabra")
        word = str(input())
        for i in range(0,len(dictionary.palabras)):
            if dictionary.palabras[i] == word:
                print("Palabra: "+ dictionary.palabras[i] + " ,Significado: " + dictionary.significados[i])
            elif dictionary.palabras[i] != word:
                print("Palabras no encontrada")
        return menu()
    else:
        print("ADIOS!!!...")

    
menu()



