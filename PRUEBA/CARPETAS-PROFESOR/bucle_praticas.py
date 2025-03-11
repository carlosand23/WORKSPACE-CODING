#Escribe un programa que sume todos los elementos de una lista de números.
#Lista = [4,2,3,1,12]
#suma = 0
#for numero in Lista:
#    suma += numero
#    print(suma)
# Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for
#for i in range(1,10):
#    print(i, end= " ")

#for i in "palabra":
#    print("Holis", end= "22  ")

# Escribe un programa que solicite al usuario un número entero positivo y luego 
# imprima la tabla de multiplicar de ese número del 1 al 10.
#numero = int(input("introduzca un numero:  "))
#for i in range(1,11):
#    print(f"{numero} X {i} = {numero * i}")
    
# Escribe un programa que solicite al usuario una cadena de texto y luego imprima cada 
# carácter de la cadena junto con su frecuencia (cuántas veces aparece en la cadena). 
# Utiliza un diccionario para almacenar las frecuencias.
#palabra_usuario = str(input("Inserta una palabra         "))
#Frecuencias = []
#for i in palabra_usuario:
#    if i in Frecuencias[]:
#        Frecuencias{i} + 1
#print(i)

#Usa un bucle for para imprimir los primeros 5 números pares (2, 4, 6, 8, 10)
#for i in range(2,11,3):
#    print(i)

#Usa un bucle for para sumar los números del 1 al 10 e imprimir el resultado
#suma = 0
#for i in range(1,11):
#    suma += i
#print(suma)

#Usa un bucle for para imprimir cada letra de una palabra.
#Palabra = "producir"
#for i in Palabra:
#    print(i)

#Usa un bucle for para imprimir los cuadrados de los números del 1 al 5.
#cuadrados = 0
#for i in range(1,6):
#    print(i**2)

#Usa un bucle for para contar cuántas vocales hay en una palabra.
#palabra = "persona"
#vocales = "aeiou"
#contador = 0
#for i in palabra:
#    if i in vocales:
#        contador += 1
#print(contador)

#Usa un bucle for para imprimir solo los números impares del 1 al 20.
#for i in range(1,21,2):
#    print(i)

#Usa un bucle for para imprimir cada nombre de una lista
#lista = ["pedro", "alejandro", "jaime", "ana"]
#for i in lista:
#    print(i)

#Usa un bucle for para generar la tabla de multiplicar de un número (por ejemplo, la tabla del 7).
#numero = 7
#for i in range(1,11):
#    print(f"{numero} X {i} = {numero * i}")

#Dada una lista de números, suma solo los números pares.
#Lista = [4,12,7,10,5]
#suma = 0
#for i in Lista:
#    if i %2 == 0:
#        suma += i 
#print(suma)

#Dada una lista de números, encuentra el número más grande.
#lista = [4,8,1,6,5,9]
#grande = 0
#for i in lista:
#    if i > grande:
#        grande = i
#print(i)

#Dada una cadena de texto, cuenta cuántas vocales hay.
#texto = "caballero"
#vocales = "aeiou"
#contador = 0

#for caracter in texto:
#    if caracter in vocales:
#        contador += 1
#print(contador)

#Dadas dos listas de números, multiplica los elementos en la 
# misma posición y almacena el resultado en una tercera lista
#lista_1 = [2,1,10,7]
#lista_2 = [9,5,2,4]
#resultado = []

#for i in range(len(lista_1)):
#    resultado.append(lista_1[i] * lista_2[i])
#print(resultado)

#Dadas dos listas de números, resta los elementos de la segunda 
# lista a los de la primera en la misma posición y almacena el resultado en una tercera lista
#lista_1 = [10,5,2,1]
#lista_2 = [9,3,8,6]
#resultado = []

#for i in range(len(lista_2)):
#    resultado.append(lista_1[i]-lista_2[i])
#print(resultado)

#Dadas dos listas de cadenas, concatena 
# los elementos en la misma posición y almacena el resultado en una tercera lista    
#lista_1 = ["Sevilla", "Granada", "Cadiz", "Chiclana"]
#lista_2 = [" Caracas", " Maracay", " Valencia", " Margarita"]
#Resultado = []

#for i in range(len(lista_1)):
#    Resultado.append(lista_1[i] + lista_2[i])
#print(Resultado)    

#Dadas dos listas de nombres y apellidos, concatena los elementos en la misma posición 
#en formato "Apellido, Nombre" y almacena el resultado en una tercera lista
#apellidos = ["Borja", "Robles", "Caceres", "Rojas"]
#nombres = ["Roberto", "Jane", "Laura", "Anne"]
#nombre_completo = []

#for i in range(len(apellidos)):
#    nombre_completo.append(apellidos[i] + " " + nombres[i])
#print(f"el nombre completo de los participantes es {nombre_completo}")

#Dada una cadena de texto, cuenta cuántas vocales hay.
#palabra = "caballeriza"
#vocales = "aeiou"
#n_vocales = 0

#for i in palabra:
#    if i in vocales:
#        n_vocales += 1
#print(n_vocales)

#Dadas dos listas de números, 
# multiplica los elementos en la misma posición y almacena el resultado en una tercera lista.
#lista_1 = [3,20,9,8,1]
#lista_2 = [1,10,2,4,77]
#resultado = []
#for i in range(len(lista_1)):
#    resultado.append(lista_1[i] * lista_2[i])
#print(resultado)
            
# Dado un string, utiliza un bucle for para contar cuántas veces aparece la 
# letra 'a' en el string
#palabra = "raperas"
#letra = "a"
#conteo = 0

#for i in palabra:
#    if i == letra:
#        conteo += 1
#print(conteo)

# Escribe un script que cuente desde 1 hasta un número n proporcionado por 
# el usuario, imprimiendo cada número
#numero = int(input("ingrese un numero:  "))

#for i in range(1,numero+1):
#        print(i)

# Crea un programa que sume números introducidos por el usuario hasta que el 
# usuario introduzca 0. Al final, el programa debe mostrar la suma total
#suma = 0
#numero = int(input("Introduce un número (0 para terminar): "))
#while numero != 0:
#    suma += numero
#    numero = int(input("Introduce otro número (0 para terminar): "))
#print("La suma total es:", suma)

#que se repita un saludo solo 5 veces
#saludo = "Hola amigo, como estas?"
#contador = 0

#while contador <= 5:
#        print(saludo)
#        contador += 1
#print("ok, no hace falta que me digas nada, ya se que estas bien")

#Escribe un programa que pida al usuario un número y luego sume todos
# los números desde 1 hasta ese número utilizando un bucle while 7 
#numero = int(input("Introduce un numero  "))
#suma = 0
#contador = 1

#while contador <= numero:
#        suma += contador 
#        contador += 1
#print(suma)

#Adivina el número:
#Crea un programa que genere un número aleatorio entre 1 y 100, y luego pida al usuario que adivine el número.
# El programa debe indicar si el número ingresado es mayor o menor que el número generado, y seguir pidiendo números
# hasta que el usuario adivine correctamente.

import random
numero_secreto = random.randint(1,100)
numero_usuario = int(input("Adivina el numero:  "))

while numero_usuario != numero_secreto:
        if numero_usuario > numero_secreto:
                print("muy alto")
        elif numero_usuario < numero_secreto:
                print("muy bajo")
        numero_usuario = int(input("Intentalo de nuevo  "))
print("Felicidades lo has logrado!")

        

    