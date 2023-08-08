class Tienda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)


    def vender_producto(self, id_producto):
        
        if id_producto >= 0 and id_producto < len(self.productos):
            producto_vendido = self.productos.pop(id_producto)
            producto_vendido.print_info()
        else:
            print("No se encontro ningun producto con es id")
    
    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, False)

class Producto: 

    def __init__(self, nombre, precio, categoria):
        self.nombre= nombre
        self.precio = precio
        self.categoria = categoria
        self.id = None
        

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100

        else:
            self.precio -= self.precio * cambio_porcentaje / 100

    def print_info(self):
        print(f"el nombre del producto es {self.nombre} el nombre de la categoria {self.categoria} es precio es de {self.precio}")
        

    

