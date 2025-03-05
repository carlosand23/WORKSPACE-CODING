import random

def Juego_de_adivinanza():
    Random_number = random.randint(1,100)
    print("Acabo de escribir un numero")

    while True:
        numero = int(input("Adivina cual es "))
        if numero > Random_number:
            print("Too high, keep trying")
        elif numero < Random_number:
            print("Too low, keep trying")
        else:
            print("Lo lograste!!!")

Juego_de_adivinanza()

    
    
