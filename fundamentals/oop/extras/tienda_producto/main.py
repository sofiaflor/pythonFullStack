from tienda import Tienda, Producto


def main():


    while True:  

        print('----------------------|Tienda TiaSofi|------------------------')
        print("1. seleccion higene")
        print("2. seleccion congelados")
        print("3. seleccion comida")
      
        option= input("seleccione una opcion:  ")

        try:
            if option == "1":
                option = input("Escoja una opcio")
                pass


            elif option == "2":
                producto2 = Producto
                producto2.print_info
                pass
                
            elif option == "3":
                pass
            
            elif option == "4":
               break
            
        except ValueError:
            print("valueError: Ingrese datos validos")

if __name__ == "__main__":
    main()

#instanciar tienda
tienda = Tienda("tíaSofi")

#instanciar producto
producto1 = Producto("confort", 3000, "higene")
producto2 = Producto("helado", 1000, "congelados")
producto3 = Producto("galletas", 2000, "comida")

#agregar producto a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)


#vender producto por id
tienda.vender_producto(1)


##print productos restantes
for producto in tienda.productos:
    producto.print_info()

#aplicar inflacion
tienda.inflacion(10)

#print info actualizada de los productos
for productos in tienda.productos:
    producto.print_info()

#tienda hace liquidacion
tienda.hacer_liquidacion("comida", 20)

#print info actual de los productos
for producto in tienda.productos:
    producto.print_info()


# def main():
#     tienda

#     while True:  

#         print('----------------------|Tienda TiaSofi|------------------------')
#         print("1.- Mostrar productos")
#         print("2.-Comprar")
#         print("3.-Salir")
      
#         option= input("seleccione una opcion:  ")

#         try:
#             if option == "1":
#                 pass

#             elif option == "2":
#                 pass
                
#             elif option == "3":
#                break
            
#         except ValueError:
#             print("valueError: Ingrese datos validos")

# if __name__ == "__main__":
#     main()


