from user import User
from libro import Libro
class Biblioteca:

    def mostrar_menu():

        print("|------------------Biblioteca Sofi-----------------|")
        print("| Opción 1: Agregar un nuevo libro a la biblioteca |")
        print("| Opción 2: Eliminar un libro de la biblioteca     |")
        print("| Opción 3: Prestar un libro de la biblioteca      |")
        print("| Opción 4: Devolver un libro a la biblioteca      |")
        print("| Opción 5: Agregar un nuevo usuario               |")
        print("| Opción 6: Eliminar un usuario                    |")
        print("| Opción 7: Ver todos los libros en la biblioteca  |")
        print("| Opción 8: Ver todos los usuarios                 |")
        print("| Opción 0: Salir de la biblioteca                 |")
        print("|--------------------------------------------------|")

    def main():
        biblioteca1 = Biblioteca()
    
    
    while True:
        mostrar_menu()
        Option = input("Escoja una Opcion:")
    
        libros = input("ingresa libro: ")
        if Option == "1":   
            nuevo_libro = Libro()
            nuevo_libro = nuevo_libro.agregar_libro()
            libros[libros] = nuevo_libro
            nuevo_libro.append(list)
            print("Se agrego el libro con exito")


        elif Option == "2":
            libros = input("Ingresa el titulo del libro: ")
            libros.eliminar_libro()
            
            

        elif Option == "3":
           nuevo_libro.prestar_un_libro() 

        elif Option == "4":
           nuevo_libro.devolver_libro()
           
        
        elif Option == "5":
            nuevo_usuario = User()
            nuevo_usuario = nuevo_usuario.crear_usuario()
            nuevo_usuario[nuevo_usuario] = nuevo_usuario
            print("Se agrego el usuario con exito")


        elif Option == "6":
          nuevo_usuario.eliminar_usuario()
        else:
            print("Option invalida, Intente nuevamente. \n")
            
if __name__ == "__main__":
   main()

