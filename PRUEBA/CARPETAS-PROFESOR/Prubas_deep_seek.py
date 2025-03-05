#vamos a crear un conversor de grados Celsius a Fahrenheit
#numero = float(input("Ingresa la temperatura en Celsius: "))
#conversion = ((numero * 9) /5 +32)
#print(f"La conversion seria: {conversion} Grados Fahrenheit")

#Pide al usuario su peso (en kg) y su altura (en metros), y calcula su Índice de Masa Corporal (IMC). 
# Luego, clasifica el IMC en:Bajo peso: IMC < 18.5  Normal: 18.5 <= IMC < 25
#Sobrepeso: 25 <= IMC < 30    Obesidad: IMC >= 30

#Peso = float(input("Ingrese su peso en Kg:   "))
#Talla = float(input("Ingrese su talla en metros: "))
#IMC = Peso / (Talla**2)
#print(f"su IMC es {IMC}")

#if IMC < 18.5:
   # print("Bajo peso")
#elif 18.5 <= IMC < 25:
 #   print("Peso normal")
#elif 25 <= IMC < 30:
  #   print("Sobrepeso")
#else:
   # print("Obesidad MORBIDA") 

#Pide al usuario que ingrese un número y muestra la tabla de multiplicar 
#de ese número del 1 al 10.

#Numero = int(input("Ingrese un numero "))

#for i in range(1, 11):
#    print(f"{Numero} X {i} = {Numero*i}")
    
# Escribe un programa que sume todos los números pares del 1 al 100.
#suma = 0
#for i in range(1,101):
 #   if i %2 == 0:
  #      suma = suma+i
#print(suma)

#Crea un programa que genere un número aleatorio entre 1 y 100, y pida al usuario 
# #que adivine el número. El programa debe indicar si el número ingresado es mayor o menor 
# #que el número generado, hasta que el usuario adivine correctamente   

#import random
#numero_random = random.randint(1,100)

#while True:
 #   numero_usuario = int(input("Ingrese un numero: "))
  #  if numero_usuario == numero_random:
   #     print("En hora buena! Lo adivinaste!")
    #    break
   # elif numero_usuario > numero_random:
    #    print("Muy alto")
    #elif numero_usuario < numero_random:
     #   print("Muy bajo")

#Escribe una función que tome un nombre como parámetro y devuelva un saludo 
# personalizado, por ejemplo: "Hola, [nombre]!"
#def Saludo(nombre):
 #   return "Hola " + nombre + ", como estas?"
#mensaje = Saludo("Pepe")
#print(mensaje)

#def factorial(n):
 #   if n > 0
  #  for i in range(1, i + 1) 

#Crea una calculadora

#creando las funciones aritmeticas de la calculadora
def suma(a,b):
    return f"Tu suma da: {a + b}" 

def resta(a,b):
    return f"Tu resta da: {a - b}"

def multiplicacion(a,b):
    return f"Tu multiplicacion da: {a * b}"

def division(a,b):
    if b == 0:
        return "Error"
    return f"Tu division da: {a / b}" 

#creando la funcion de la calculadora 
#comienzo a colocar los textos que vera el usuario
def calculadora():
    print("Bienvenidos a la calculadora básica")
    print("A continuación te presentamos las opciones que tenemos disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    
    operacion = input("Ingresa el numero de la operacion:  ")    

#solicitar 2 numeros
    if operacion in ("1","2","3","4"):
        num1 = float(input("ingresa el primer numero: "))
        num2 = float(input("ingresa el segundo numero "))

    elif operacion == "1":
        print(suma(num1,num2))
    elif operacion == "2":
        print(resta(num1,num2))
    elif operacion == "3":
        print(multiplicacion(num1,num2))
    elif operacion == "4":
        print(division(num1,num2))
    else:
        print("Error. Solo puedes introducir numeros del 1 al 4")
        

calculadora()