class UsuarioExiste(Exception):
    pass

class UsuarioNoExiste(Exception):
    pass

class Usuario:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def cambiar_contraseña(self, nueva_contraseña):
        self.password = nueva_contraseña
        print("Contraseña cambiada exitosamente.")

class Invitado(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo, "invitado")

class Administrador(Usuario):
    def __init__(self, nombre, correo, password):
        super().__init__(nombre, correo, password)

    def eliminar_usuario(self, usuario, Sistema):
        Sistema.eliminar_usuario(usuario)

    def modificar_usuario(self, usuario, nuevo_nombre, nuevo_correo, Sistema):
        if usuario not in Sistema.usuarios:
            raise UsuarioNoExiste("El usuario no existe en el Sistema.")
        usuario.nombre = nuevo_nombre
        usuario.correo = nuevo_correo
        print("Usuario modificado exitosamente.")

    def listar_usuarios(self, Sistema):
        print("Lista de usuarios:")
        for usuario in Sistema.usuarios:
            print(f"Nombre: {usuario.nombre} - Correo: {usuario.correo}")

class Sistema:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        for u in self.usuarios:
            if u.nombre == usuario.nombre:
                raise UsuarioExiste("El usuario ya existe en el Sistema.")
        self.usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        if usuario not in self.usuarios:
            raise UsuarioNoExiste("El usuario no existe en el Sistema.")
        self.usuarios.remove(usuario)