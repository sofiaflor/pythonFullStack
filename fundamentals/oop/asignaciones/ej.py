# #declarar una clase y darle el nombre de usuario
# class Usuario:
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.balance_cuenta = 0

# Usuario()
# guido = Usuario()
# monty = Usuario()
# print(guido.name) 
# print(monty.name) 


# class Usuario:
#     # declarando un atributo de clase
#     nombre_banco = "Primer Dojo Nacional"		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.balance_cuenta = 0

# guido = Usuario()
# monty = Usuario()
# guido.nombre_banco = "Dojo Credit Union"
# print(guido.nombre_banco) # salida: Dojo Credit Union 
# print(monty.nombre_banco) # salida: Primer Dojo Nacional


class Usuario:
# los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
# ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount
sara = Usuario("sara" , "sara@gmail.com") 
cami = Usuario("cami" , "cami@gmail.com")         
samy = Usuario("samy" , "samy@gmail.com")         
vale = Usuario("vale" ,"vale@gmail.com")        
sofi = Usuario("sofi" , "sofi@gmail.com")
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")

vale.hacer_depósito(100000000)
sofi.hacer_depósito(200000000)
samy.hacer_depósito(150000)
cami.hacer_depósito(300000)
sara.hacer_depósito(500)



print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python


print(f"mi nombre es {vale.name} y mi correo es {vale.email} y mi balance de cuenta es {vale.balance_cuenta}")
print(f"mi nombre es {samy.name} y mi correo es {samy.email} y mi balance de cuenta es {samy.balance_cuenta}")
print(f"mi nombre es {sofi.name} y mi correo es {sofi.email} y mi balance de cuenta es {sofi.balance_cuenta}")
print(f"mi nombre es {cami.name} y mi correo es {cami.email} y mi balance de cuenta es {cami.balance_cuenta}")
print(f"mi nombre es {sara.name} y mi correo es {sara.email} y mi balance de cuenta es {sara.balance_cuenta}")


