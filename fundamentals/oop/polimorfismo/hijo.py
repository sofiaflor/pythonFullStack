from padre import padre

class hijo(padre):
    def __init__(self, huerfano) -> None:
        self.huerfano = huerfano

    def imprimir(self):
        return f"{self.huerfano}"
    
papá = padre()
hijo = hijo()
papá.method_a()
hijo.method_a()    