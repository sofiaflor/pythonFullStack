from mascota import Mascota
class ninja():
    def __init__( self, name, apellido, premios, comida_mascota, mascota):
        self.name = name
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(cls, self):
        self.Mascota.jugar()
        return self
        




    def alimentar(self):
        if len(self.comida_mascota)> 0:
         comida_mascota = self.comida_mascota.pop()
         print(f"alimentacion {self.mascota.nombre} {comida_mascota}")
         self.mascota.comida_mascota()

        else:
            print("oh no! tu necesitas darle comida a tu mascota")
        return self
        




    def bañar(self):
        self.mascota.ruido()
        return self
        
golosinas = ['Snausage','Bacon',"Trash Bag"]
comida_mascota = ['Pizza','Burger']



    # implementa los siguientes métodos:
    # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    # alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    # bañar(): limpia la mascota del ninja invocando el método de mascota sonido()






