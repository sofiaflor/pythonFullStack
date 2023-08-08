class Calculadora:
    sum = 0
    sum1= 0

    def __init__(self, sum, sum1):
        self.sum = int(sum)
        self.sum1 = int(sum1)
        
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

# sum = int(input('numero: '))
# sum1 = int(input('numero: '))

# calculadora = calculadora(sum , sum1)

def main():
    calculadora = Calculadora(0,0)

    while True:  

        print('----------------------Calculadora------------------------')
        print("1.- Sumar")
        print("2.-restar")
        print("3.-multiplicar")
        print("4.-dividir")
        print("5. Salir")
        option= input("seleccione una opcion:  ")

        try:
            if option == "1":
                sum = input("ingresa numero:  ")
                sum1 = input("ingresa numero:  ")
                calculadora = Calculadora(sum, sum1)
                resultado = calculadora.sumar()
                print("El resultado de la suma es:", resultado)

            elif option == "2":
                sum = input("ingresa numero:  ")
                sum1 = input("ingresa numero:  ")
                calculadora = Calculadora(sum, sum1)
                resultado = calculadora.restar()
                print("El resultado de la suma es:", resultado)
                
            elif option == "3":
                sum = input("ingresa numero:  ")
                sum1 = input("ingresa numero:  ")
                calculadora = Calculadora(sum, sum1)
                resultado = calculadora.multiplicar()
                print("El resultado de la suma es:", resultado)
                
            elif option == "4":
                sum = input("ingresa numero:  ")
                sum1 = input("ingresa numero:  ")
                calculadora = Calculadora(sum, sum1)
                resultado = calculadora.dividir()
                print("El resultado de la suma es:", resultado)

            elif option == "5":
                break
        except ValueError:
            print("valueError: Ingrese datos validos")

if __name__ == "__main__":
    main()
    