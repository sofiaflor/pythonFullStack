from ninja import ninja
from mascota import Mascota

inuyasha = ninja('inuyasha', '-', 100,100, "kira")
kirara = Mascota('kirara', 'zorro', 'ramen')

kirara.dormir()
kirara.comer()

kirara.mostrarEnergia()
kirara.mostrarsalud()