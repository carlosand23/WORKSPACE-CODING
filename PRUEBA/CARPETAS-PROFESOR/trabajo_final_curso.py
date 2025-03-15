#Título: Sistema de Gestión de Biblioteca
#Descripción: Eres el desarrollador de un sistema básico de gestión para una biblioteca. Debes crear un programa en Python 
# que permita registrar libros y gestionar préstamos a usuarios. El programa debe cumplir con los siguientes requisitos:
#1.Clase Libro:
#•Crea una clase Libro con los atributos titulo (str), autor (str), isbn (str) y disponible (bool, inicialmente True).
#•Incluye un método agregar() que permita introducir un nuevo libro con sus características.
#•Incluye un método prestar() que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje 
# si ya está prestado.
#•Incluye un método devolver() que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje 
# si ya estaba disponible.
#•Incluye un método mostrar() que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla 
# con todos sus datos y diga si estás disponible o no.
#•Incluye un método buscar() que busque un libro en concreto por su ISBM y lo muestre en pantalla con todos sus datos 
# y diga si está disponible o no.

libreria = []

class Libro():
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo 
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    
    def agregar(self):
        
    