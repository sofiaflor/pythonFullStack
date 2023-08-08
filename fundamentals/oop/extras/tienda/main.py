from tienda import tienda
from producto import producto


def mostrar_menu():
    print("|----------------Tienda---------------|")
    print("| Opción 1: Registrar nuevo Producto  |")
    print("| Opción 2: Registrar una venta       |")
    print("| Opción 3: Listar Productos          |")
    print("| Opción 4: Actualizar Productos      |")
    print("| Opción 0: Salir                     |")
    print("|-------------------------------------|")

def main():
    tienda1 = tienda("tiasofi")
    while True:
        mostrar_menu()
        Option = input("Escoja una Opcion:")

        if Option == "1":
            print("+--------------------------------+")
            print("|-------Ingresar Nombre----------|")
            print("+--------------------------------+")
            Nombre = input("ingrese el nombre del producto:")
            Precio = input("ingrese el precio:")
            Categoria = input("ingrese la categoría :")
            nuevo_producto = producto(Nombre, Precio, Categoria)
            tienda1.agregar_producto(nuevo_producto)
            print("+--------------------------------+")
            print("|--------Producto Creado---------|")
            print("+--------------------------------+")
           

        if Option == "2":
            pass

        if Option == "3":
            tienda1.listar_productos()

        if Option == "4":
            print("+--------------------------------+")
            print("|-------Ingresar Nombre----------|")
            print("+--------------------------------+")
            Nombre = input("ingrese el nombre del producto:")
            Precio = input("ingrese el precio:")
            Categoria = input("ingrese la categoría :")
            nuevo_producto = producto(Nombre, Precio, Categoria)
            tienda1.modificar_producto(nuevo_producto)
            print("+--------------------------------+")
            print("|--------Producto modificado---------|")
            print("+--------------------------------+")
           

        if Option == "0":
            print("¡Hasta Luego!")
            break

        else:
            print("Option invalida, Intente nuevamente. \n")

if __name__ == "__main__":
    main()