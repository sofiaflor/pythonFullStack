class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interés, balance):
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)
    
    def depósito(self, amount):
       self.amount =+ amount
    
    def retiro(self, amount):
        self.amount -= amount
    
    def mostrar_info_cuenta(self):
        for i in CuentaBancaria.cuentas:
            print(f"balance : ${i.mostrar_info_cuenta}")
        print(CuentaBancaria.generar_interés())
        return self
    
    @classmethod
    def generar_interés(cls, tasa_interés):
        num = tasa_interés
        for i in cls.cuentas:
            num * i.balance
        
        
cuenta = CuentaBancaria(1.5 , 1000)
cuenta1 = CuentaBancaria(1.5 , 500)


cuenta.depósito(5000)
cuenta.mostrar_info_cuenta()
cuenta.generar_interés()

# class CuentaBancaria:
#     # cuentas = []
#     def __init__(self, tasa_interés, balance):
#         self.tasa_interés = tasa_interés
#         self.balance = balance
#         # CuentaBancaria.cuentas.append(self)
    
#     def depósito(self, amount):
#        self.amount =+ amount
    
#     def retiro(self, amount):
#         self.balance -= amount
    
#     def mostrar_info_cuenta(self):
#         return f"el balance de la cuenta es: ${self.balance}"
    
#     def generar_interés(self):
#         if self.balance > 0:
#             self.balance += (self.balance*self.tasa_interés)
#         return self

        
# cuentaSofia = CuentaBancaria(.5 , 1000)
# cuentaSofia.mostrar_info_cuenta()