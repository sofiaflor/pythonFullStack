class CuentaBancaria:
    # atributo de clase
    
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self,tasa_int,balance):
        self.id =+ 1
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    
    # método de clase para cambiar el nombre del banco
    @classmethod
    def cambiar_nombre_banco(cls,name):
        cls.nombre_banco = name
    # método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase 
        for account in cls.todas_las_cuentas:
            sum += account.balance
        return sum
    
    def imprime(self):
        print("estas son todas las cuentas")
        for account in CuentaBancaria.todas_las_cuentas:
            print(f"tasa de interes = {account.tasa_int} y el total de la cuenta es de {account.balance}")
        print("Este es el total de las cuentas  ")
        print("-"*20  + " " + "-"*20 )
        print(CuentaBancaria.todos_los_balances())
        return self
    

cuenta1 = CuentaBancaria(1.5,100000)
cuenta1 = CuentaBancaria(1.5,100000)
cuenta1 = CuentaBancaria(1.5,100000)
cuenta1 = CuentaBancaria(1.5,100000)
cuenta1 = CuentaBancaria(1.5,100000)

cuenta1.todos_los_balances()

cuenta1.imprime()