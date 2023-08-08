from cue import cuentaBancaria

class Usuario:
    def __init__(self, name):
        self.name = name
        self.cuenta = cuentaBancaria(.02, 0)	# añadió esta línea

    def mostrar_balance(self):

        info = print(f"Saldo de {self.name} es: ${self.cuenta.balance}")
        return info
    
    def deposito(self,monto, usuario):
        self.balance -= monto
        usuario.balance += monto
        self.mostrar_balance()
        usuario.mostrar_balance()
        return self