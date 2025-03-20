#crear una clase estudiante que tenga los atributos: nombre, edad y grado, 
# crear metodo "estudiar" que diga "el estudiante nombre esta estudiando"
#se debe interactuar con el usuario y este debe brindar los atributos
#class Estudiante:
#    def __init__(self, nombre, edad, grado):
#        self.nombre = nombre
#        self.edad = edad
#        self.grado = grado
        
#    def estudiar(self):
#        print(f"El estudiante {self.nombre} está estudiando")
            
        
#estudiante1 = Estudiante(input("Ingrese nombre del estudiante: "), input("ingresa la edad: "), input("ingresa el grado: "))
#estudiante1.estudiar()

#Crea una clase llamada Coche que tenga los siguientes atributos:
#marca (str): La marca del coche.
#modelo (str): El modelo del coche.
#color (str): El color del coche.
#Además, define un método llamado acelerar que imprima: "El coche {marca} {modelo} de color {color} está acelerando."
# Interacción con el usuario: Pide al usuario que ingrese la marca, modelo y color del coche.
#Crea un objeto de la clase Coche con los datos proporcionados. Llama al método acelerar.
#class Coche():
#    def __init__(self, marca, modelo, color):
#        self.marca = marca
#        self.modelo = modelo
#        self.color = color
        
#    def Acelerar(self):
#        print(f"El coche {self.marca}, {self.modelo}, de color {self.color} está acelerando.")
        
#marca = input("Ingresa la marca de tu coche:  ")
#modelo = input("Ingresa el modelo: ")
#color = input("Ingresa el color: ")

#coche1 = Coche(marca, modelo, color)
#coche1.Acelerar()

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def Hablar(self):
        print("Hola amigo, como estas")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def MostrarHabilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad, salario, empresa):
        Persona().__init__(nombre, edad, nacionalidad)
        Artista().__init__(habilidad)
        self.salario = salario
        self.empresa = empresa 
        
    
  
        


jorge = Empleado("Jorge", 35, "venezolano", "programador", 2500)
juan = Estudiante("Juan", 19, "ecuatoriano", 9.5, "UDLA")
print(jorge.nacionalidad)
jorge.Hablar()

print(juan.universidad)  
juan.Hablar()




  
        
        
    
    





    