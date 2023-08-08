def main():
    while True:

        print('----------------------------------------Gestión de Usuario----------------------------------------')
        option = input("Seleccione una opcion:  ")


        try:
            if option == "1":
                nombre = input("Ingresa el nombre: ")
                correo = input("Ingresa el correo: ")
                contraseña = input("Ingresa la contraseña: ")
                agregar_usuario = Usuario(nombre, correo, contraseña)
                Sistema.agregar_usuario(agregar_usuario)

            elif option == "2":
                nombre = input("Ingresa tu nombre: ")
                for Usuario in Sistema.Usuarios:
                    if Usuario.nombre == nombre:
                        nueva_contraseña = input("Ingresa tu nueva contraseña: ")
                        Usuario.cambiar_contraseña(nueva_contraseña)
                        break
                else:
                    raise UsuarioNoExiste("El usuario no existe en el Sistema.")

            elif option == "3":
                nombre = input("Ingresa el nombre del usuario a modificar: ")
                for Usuario in Sistema.suarios:
                    if Usuario.nombre == nombre:
                        nuevoNombre = input("Ingresa el nuevo nombre: ")
                        nuevoCorreo = input("Ingresa el nuevo correo: ")
                        Administrador = Administrador("", "", "")
                        Administrador.modificar_usuario(
                            Usuario, nuevoNombre, nuevoCorreo, Sistema)
                        break
                else:
                    raise UsuarioNoExiste(
                        "El usuario no existe en el Sistema.")

            elif option == "4":
                Administrador = Administrador("", "", "")
                Administrador.listar_usuarios(Sistema)

            elif option == "5":
                break
        except UsuarioExiste as ue:
            print(ue)
        except UsuarioNoExiste as une:
            print(une)


if __name__ == "__main__":
    main()