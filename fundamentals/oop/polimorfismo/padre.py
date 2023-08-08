class padre:
    def __init__(self, name) -> None:
        self.name = name

    def imprimir(self):
        return f"{padre.imprimir}"
    
class hijo(padre):
    def method_a(self):
        print("invocando método_a HIJO")
papá = padre()
hijo = hijo()
papá.method_a()
hijo.method_a() # Nota que esto anula el método Padre


