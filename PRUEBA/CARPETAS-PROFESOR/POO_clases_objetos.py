#Funcion constructora:
class Celular:
    def __init__(self, marca, modelo,camara):
        self.marca = marca 
        self.modelo = modelo
        self.camara = camara 
        
    def llamar(self):
        print(f"estas haciendo una llamada desde tu {self.modelo}")
    
    def cortar(self):
        print(f"Acabas de cortar la llamada desde tu: {self.modelo}")    
        
        
Celular1 = Celular("Apple", "12 Pro Max", "48MP")
CelularSamsung = Celular("Samsung", "S22", "62MP")

Celular1.cortar()