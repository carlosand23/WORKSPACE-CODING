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

biblioteca = []

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo 
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    
    def prestar(self):
        if self.disponible is True:
            self.disponible = False
            print(f"El libro {self.titulo} ha sido prestado")
        else:
            print(f"El libro {self.titulo} no esta disponible")
        
    def devolver(self):
        if self.disponible is False:
            self.disponible = True
            print(f"El libro {self.titulo} ha sido devuelto")
        else:
            print(f"El libro {self.titulo} ya estaba disponible")
    
    def mostrar(self):
        estado = "Disponible"
        if self.disponible is True:
            estado = "Disponible"
        else:
            estado = "No Disponible"
        print(f" Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}")
              

def agregar_libro(titulo, autor, isbn):
    libro = Libro(titulo, autor, isbn)
    biblioteca.append(libro) 
    print(f"El libro {titulo} se agrego de forma correcta a la biblioteca")

def buscar_libro(isbn):
    for libro in biblioteca:
        if libro.isbn == isbn:
            print("Libro encontrado:")
            libro.mostrar()
            return
    print(f"No se encontro el ISBN: {isbn}")

def menu():
    print("\nBienvenido a la Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")
    return input("Elige una opción: ")

def main():
    biblioteca = []

    while True:
        opcion = menu()

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, isbn)
            agregar_libro(titulo, autor, isbn)
            

        elif opcion == "2":
            isbn = input("Ingresa el ISBN: ")
            encontrado = False
            for libro in biblioteca:
                if libro.buscar(isbn):
                    encontrado = True
                    libro.prestar()
                    break
            if not encontrado:
                print("Libro no encontrado.")

        elif opcion == "3":
            isbn = input("Ingresa el ISBN: ")
            encontrado = False
            for libro in biblioteca:
                if libro.buscar(isbn):
                    encontrado = True
                    libro.devolver()
                    break
            if not encontrado:
                print("Libro no encontrado.")

        elif opcion == "4":
            if not biblioteca:
                print("No hay libros en el inventario.")
            else:
                for libro in biblioteca:
                    libro.mostrar()

        elif opcion == "5":
            isbn = input("Ingresa el ISBN: ")
            encontrado = False
            for libro in biblioteca:
                if libro.buscar(isbn):
                    encontrado = True
                    break
            if not encontrado:
                print("Libro no encontrado.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, elige una opción válida.")

#if __name__ == "__main__":
#    main()