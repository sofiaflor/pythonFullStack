class producto:
    def __init__(self, nombre, precio, categoría):
        self.nombre = nombre
        self.precio = precio
        self.categoría = categoría

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100

        else:  
            self.precio -= self.precio * cambio_porcentaje / 100
    
    def imprimir(self):
        print(f"el nombre del producto es {self.nombre} el nombre de la categoría es {self.categoría} el precio es de {self.precio}")
