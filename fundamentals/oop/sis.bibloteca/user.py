class User:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.lista_usuarios = []
        self.libros_prestados =[]

    def crear_usuario(self):
        print("Crear Usuario.... ")
        nombre = input("Ingresar nombre: ")
        id = input("Ingresar id:")

        self.nombre = nombre
        self.id = id

    
    def eliminar_usuario(self, nombre):
        for x in self.lista_usuario:
            if x.nombre == nombre:
                x.remove 
        return self   
