class cuentaBancaria:

    def __init__(self,interes,balance):
        self.interes=interes
        self.balance=balance

    
    def deposito(self,monto):
        self.balance += monto
        return self

    def retiro(self,monto):
        if(self.balance - monto ) >= 0:
            self.balance -= monto
        else:
            print(f" saldo no disponible , :( tu saldo es {self.balance}")
        return self
    
    def mostrar_info_cuenta(self):

        info = print(f"Saldo de {self.usuario} es: ${self.balance}")
        return info
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interes)
        return self




# cuentaSofia = cuentaBancaria(.25,1000,"Sofia")
# cuentaVale=cuentaBancaria(.5,1000000,"Valentina")

# cuentaSofia.retiro(2000).deposito(5000).deposito(1500).deposito(2000).mostrar_info_cuenta()
# cuentaVale.deposito(20000).deposito(10000).retiro(100000).retiro(2000).retiro(200000).retiro(10000).mostrar_info_cuenta()
