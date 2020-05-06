class Entero:
    def __init__(self,numero):
        self.numero = numero
    def __add__(self,otro):
        return self.numero + otro.numero
        
n1 = Entero(1)
n2 = Entero(9)
n3 = n1+n2
print(n3)