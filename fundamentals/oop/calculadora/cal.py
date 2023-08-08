class calculadora:

    sum = 0
    sum1= 0

    def __init__(self, sum, sum1):
        self.sum = sum
        self.sum1 = sum1
        
    def sumar(self):
        suma = self.sum + self.sum1
        return suma
        

    def restar(self):
        resta = self.sum - self.sum1
        return resta

    def multiplicar(self):
        multiplicar = self.sum * self.sum1
        return multiplicar


    def dividir(self):
        dividir = self.sum / self.sum1
        return dividir

