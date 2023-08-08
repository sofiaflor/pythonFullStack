class Mascota:
    def __init__(self, name , tipo , golosinas ):
        self.name = name
        self.tipo = tipo
        self.golosina = golosinas
        self.salud = 100
        self.energia = 100


    def dormir(self):
        self.energia += 25
        


    def comer(self):
        self.energia += 5
        self.salud += 10
        



    def jugar(self):
        self.salud += 5
        

    def ruido(self):
        self.mascota.ruido

    def mostrarEnergia(self):
        
        print(f"tu energia es  {self.energia}")
        return self

    def mostrarsalud(self):
        
        print(f"tu salud es  {self.salud}")
        return self
    # implementa los siguientes métodos:
    # dormir() - incrementa la energía de la mascota en 25
    # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    # jugar() - incrementa la salud de la mascota en 5
    # ruido() - imprime el sonido que produce la mascota