class tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.list=[]

    def agregar_producto(self, nuevo_producto):
        self.list.append(nuevo_producto)
        return self
    
    def vender_producto(self, id):
        for x in self.list:
            if x.nombre == id:
                x.remove
            else:
                print("El producto no existe")
        return self
    
    def modificar_producto(self, producto):
        for x in self.list:
            if x.nombre == producto.nombre:
                x.nombre = id
                x.precio = producto.precio
                x.categoria = producto.categoria
                print("Producto modificado con exito")
            else:
                print("El producto no existe")
        return self
    
    
    def listar_productos(self):
        for x in self.list:
            x.imprimir()
        return self
        
    