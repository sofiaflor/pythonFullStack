class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def agregar(self, nombreUsuario):
        nombreUsuario = input("ingresa nombre: ")
        self.nombre = nombreUsuario
         

class registro:
    def __init__(self, usuario, tiempo):
        self.usuario = usuario
        self.tiempo = tiempo
        self.registro = []

    def registrar_entrada(nombre, presente):
        pass

        

class SistemaAsistencia:
    def __init__(self):
        self.usuarios = []


    def agregar_usuario(self, Usuario):
        for u in self.usuarios:
            u.nombre == Usuario.nombre
            self.usuarios.append(Usuario) 


Sofia = Usuario("Sofia","Arias")
nuevoNombre = input("Ingresa una: ")
Sofia.agregar(nuevoNombre)

print(Sofia.nombre      )