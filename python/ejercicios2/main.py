# Ejercicios python -> IF - ELSE

# Ejercicios 1: vida de una persona

# Reglas:Si la persona tiene:
# entre 0 y 3 de edad retonar infante
# entre 3 y 10 de edad retornar nino
# entre 10 y 17 adolsecente
# entre 17 y 60 adulto
# de 60 hacia adelante anciano
def person_life(age):
    numero=None;
    if age>=0 and age<3:
        numero="Infante"
    elif age>=3 and age<10:
        numero="Niño"
    elif age>=10 and age<17:
        numero="Adolescente"
    elif age>=17 and age<60:
        numero="Adulto"
    else:
        numero="anciano"
    return numero
# Ejercicio 2: Rango de edad
# Usando las reglas anteriores, si yo ingreso
# una edad de vida, deberia imprimi el rango de edad
# de ser una opcion no validd, deberi imprimir un error
def age_range(age):
    numero=None;
    if age=="infante":
        numero="0-3"
    elif age=="niño":
        numero="3-10"
    elif age=="adolescente":
        numero="10-17"
    elif age=="adulto":
        numero="17-60"
    elif age=="anciano":
        numero="60-màs"
    else:
        numero="No existe"
    return numero

# Ejercicio 3: price
# Reglas:
# Si precio < 10 retorna barato
# Si precio >= 10 y precio <= 60 retorna regular
# Si precio > 60 retorna caro 

def prices(price):
    numero=int(price)
    precio:None
    if numero>=0 and numero<10:
        return "Barato"
    elif numero>=10 and numero<=60:
        return "Regular"
    else:
        return "Caro"

## Ejercicio 4: Menus de un restaurante
## Los menus de un restaurante estan compuestos de bebidas y comidas
## Los alimetos son Saludables(S) o no saludables (NS)
## Las bebidas son "Refreso. (S), te (S) y gaseosa (NS)"
## Las comidas son "frituras (NS), ensaladas(S), Postres(NS)"
## Si el menu lleva una comida o bebida no saludable retorna "NS"
## caso contrario retorna "S"

def menus(drink, food):
    if not(drink=="Refreso" or drink=="te" or drink=="gaseosa"):
        return "Error: Opcion no valida"
    if not(food=="frituras" or food=="ensaladas" or food=="Postres"):
        return "Error: Opcion no valida"
    if drink=="Refreso" or drink=="te" and food=="ensaladas":
        return "S"
    elif not(drink=="Refreso" or drink=="te" and food=="ensaladas"):
        return "NS"
    
print("Ejercicio 1")
print(person_life(5)) #  Rpta: "nino"
print(person_life(80)) #  Rpta: "anciano"
print(person_life(15)) #  Rpta: "adolescente"
print("Ejercicio 2")
print(age_range("adolescente")) #  Rpta: "10 - 17"
print(age_range("infante")) #  Rpta: "0 - 3"
print(age_range("joven")) #  Rpta: "Error: Opcion no existente"
print("Ejercicio 3")
print(prices("100")) # Rpta: "caro"
print("Ejercicio 4")
print(menus("Refreso","ensaladas")) # Rpta: "S"
print(menus("gaseosa","ensaladas")) # Rpta: "NS"
print(menus("te","pollo")) # Rpta: "Error: Opcion no valida"