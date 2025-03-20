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
        if self.disponible:
            self.disponible = False
            print(f"El libro {self.titulo} ha sido prestado")
        else:
            print(f"El libro {self.titulo} no está disponible")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro {self.titulo} ha sido devuelto")
        else:
            print(f"El libro {self.titulo} ya estaba disponible")

    def mostrar(self):
        estado = "Disponible" if self.disponible else "No Disponible"
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}")

class Main:
    def __init__(self):
        pass

    def agregar_libro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        libro = Libro(titulo, autor, isbn)
        biblioteca.append(libro)
        print(f"El libro {titulo} se agregó correctamente a la biblioteca")

    def buscar_libro(self, isbn):
        for libro in biblioteca:
            if libro.isbn == isbn:
                print("Libro encontrado:")
                libro.mostrar()
                return libro
        print(f"No se encontró el libro con ISBN: {isbn}")
        return None

    def menu(self):
        print("\nBienvenido a la Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro por ISBN")
        print("6. Salir")
        return input("Elige una opción: ")

    def main(self):
        while True:
            opcion = self.menu()

            if opcion == "1":
                self.agregar_libro()

            elif opcion == "2":
                isbn = input("Ingresa el ISBN: ")
                libro = self.buscar_libro(isbn)
                if libro:
                    libro.prestar()

            elif opcion == "3":
                isbn = input("Ingresa el ISBN: ")
                libro = self.buscar_libro(isbn)
                if libro:
                    libro.devolver()

            elif opcion == "4":
                if not biblioteca:
                    print("No hay libros en la biblioteca.")
                else:
                    for libro in biblioteca:
                        libro.mostrar()

            elif opcion == "5":
                isbn = input("Ingresa el ISBN: ")
                self.buscar_libro(isbn)

            elif opcion == "6":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    app = Main()
    app.main()