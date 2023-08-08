import random

class Personaje:
    def __init__(self, nombre, salud, ataque_min, ataque_max):
        self.nombre = nombre
        self.salud = salud
        self.ataque_min = ataque_min
        self.ataque_max = ataque_max

    def atacar(self):
        return random.randint(self.ataque_min, self.ataque_max)

    def recibir_ataque(self, ataque):
        self.salud -= ataque

    def esta_vivo(self):
        return self.salud > 0

ninja = Personaje("Ninja", salud=100, ataque_min=10, ataque_max=20)
pirata = Personaje("Pirata", salud=100, ataque_min=10, ataque_max=25)

while ninja.esta_vivo() and pirata.esta_vivo():
    # Turno del ninja
    ataque_ninja = ninja.atacar()
    pirata.recibir_ataque(ataque_ninja)
    print(f"El Ninja ataca al Pirata con {ataque_ninja} de daño. Salud del Pirata: {pirata.salud}")

    # Verificar si el pirata fue derrotado por el ataque del ninja
    if not pirata.esta_vivo():
        break

    # Turno del pirata
    ataque_pirata = pirata.atacar()
    ninja.recibir_ataque(ataque_pirata)
    print(f"El Pirata ataca al Ninja con {ataque_pirata} de daño. Salud del Ninja: {ninja.salud}")

if ninja.esta_vivo():
    print("El Ninja ha ganado la pelea.")
else:
    print("El Pirata ha ganado la pelea.")