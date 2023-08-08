local_val = "unicornios mágicos"
def square(x):
    return x * x
class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"

class Producto:
    def __init__(self,name):
        self.name = name
        self.balance = 1000

    def agregarimpuesto(self,iva):
        self.balance *= iva

print(square(5))
Sofi = Usuario("Sofi")
print(Sofi.name)
print(Sofi.di_hola())
print(__name__)

if __name__ == "__main__":
    print("el archivo se está ejecutando directamente")
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)
  
if __name__ == "__main__":
    args = [0]
    producto = Producto([args])
    print(producto)
    print(producto.agregarimpuesto(0.18))
