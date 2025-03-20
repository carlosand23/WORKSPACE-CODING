#creando clases
#Funcion constructora:
#class Celular:
#    def __init__(self, marca, modelo,camara): #a continuacion los atributos de la clase:
#        self.marca = marca 
#        self.modelo = modelo
#        self.camara = camara 
#creando metodos        
#    def llamar(self):
#        print(f"estas haciendo una llamada desde tu {self.modelo}")
    
#    def cortar(self):
#        print(f"Acabas de cortar la llamada desde tu: {self.modelo}")    
        
        
#Celular1 = Celular("Apple", "12 Pro Max", "48MP")
#CelularSamsung = Celular("Samsung", "S22", "62MP")

#Celular1.cortar()

#Ejercicio 1: Polimorfismo con Figuras Geométricas
#Crea una clase base llamada Figura con un método area(). Luego, crea varias clases derivadas como:
# Circulo, Rectangulo y Triangulo que sobrescriban el método area(). 
# Finalmente, crea una lista de figuras y calcula el área de cada una
#class Figura:
#    def area(self):
#        pass
    
#class Circulo(Figura):
#    def __init__(self, radio):
#        self.radio = radio
    
#    def area(self):
#        return 3,1416 * self.radio ** 2

#class Rectangulo(Figura):
#    def __init__(self, ancho, alto):
#        self.ancho = ancho
#        self.alto = alto

#    def area(self):
#        return self.ancho * self.alto

#class Triangulo(Figura):
#    def __init__(self, base, altura):
#        self.base = base
#        self.altura = altura
    
#    def area(self):
#        return (self.base * self.altura)/2

#figuras = [Circulo(4), Rectangulo(4,3), Triangulo(4,4)]

#for figura in figuras:
#    print(f"El area de la figura es: {figura.area()}")

#creando clase para carros
class Coche:
    largo = 100  
    ancho = 120
    ruedas = 4
    peso = 900
    color = "azul"
    is_enMarcha = False
    
    def arrancar(self):
        self.is_enMarcha = True
    
    def estado(self):
        if (self.is_enMarcha == True):
            return "el coche esta arrancado"
        else:
            return "el coche esta parado"

#declaramos la instancia de clase
micoche1 = Coche()
print(micoche1.estado())
    
    
    
    
    
