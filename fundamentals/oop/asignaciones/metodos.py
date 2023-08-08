class Usuario:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
        

    def hacer_depósito(self, amount):
        self.amount += amount
        return self

    def hacer_retiro(self, amount):
        self.amount -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"mi nombre es {self.name} y mi balance ${self.amount}")

    def trasnferir(self, amount, otro_usuario):
        self.amount -= amount
        otro_usuario.amount += amount
        self.mostrar_balance_usuario()
        otro_usuario.mostrar_balance_usuario()
        return self
    
sofia = Usuario()

sofia.hacer_retiro
