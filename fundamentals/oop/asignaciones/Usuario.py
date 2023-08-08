class Usuario:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def hacer_depósito(self, amount):
        self.amount += amount

    def hacer_retiro(self, amount):
        self.amount -= amount

    def mostrar_balance_usuario(self):
        print(f"mi nombre es {self.name} y mi balance {self.amount}")

    def trasnferir(self, amount, otro_usuario):
        self.amount -= amount
        otro_usuario.amount += amount
        self.mostrar_balance_usuario()
        otro_usuario.mostrar_balance_usuario()


vale = Usuario("vale")
sofi = Usuario("sofi")
samy = Usuario("samy")

vale.trasnferir(200,samy)


sofi.hacer_depósito(1000)
sofi.hacer_depósito(100)
samy.hacer_depósito(700)
vale.hacer_depósito(600)
vale.hacer_depósito(100)
vale.hacer_depósito(300)


vale.hacer_retiro(200)
samy.hacer_retiro(50)
sofi.hacer_retiro(400)
sofi.hacer_retiro(50)
samy.hacer_retiro(100)
samy.hacer_retiro(20)
samy.hacer_retiro(80)

vale.mostrar_balance_usuario()
samy.mostrar_balance_usuario()
sofi.mostrar_balance_usuario()
