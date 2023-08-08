num1 = 42 #variable declaracion
num2 = 2.3 #variable declaracion
boolean = True #dato booleano
string = 'Hello World' #cadena de texto
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #arreglo, cadena de texto
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dato booleano, log statement
fruit = ('blueberry', 'strawberry', 'banana') #lista, cadena de texto
print(type(fruit)) #imprime valor o valor solicitado
print(pizza_toppings[1]) #imprime valor o valor solicitado
pizza_toppings.append('Mushrooms')
print(person['name']) #imprime valor o valor solicitado
person['name'] = 'George' #variable declaracion
person['eye_color'] = 'blue' #variable declaracion                
print(fruit[2]) #imprime valor o valor solicitado

if num1 > 45: #condicional
    print("It's greater") #imprime valor o valor solicitado 
else: #condicional
    print("It's lower") #imprime valor o valor solicitado

if len(string) < 5: #condicional
    print("It's a short word!") #imprime valor o valor solicitado
elif len(string) > 15: #condicional
    print("It's a long word!") #imprime valor o valor solicitado
else:#condicional
    print("Just right!") #imprime valor o valor solicitado

for x in range(5): #bucle for
    print(x) #imprime valor o valor solicitado
for x in range(2,5): #bucle for
    print(x) #imprime valor o valor solicitado
for x in range(2,10,3): #bucle for
    print(x) #imprime valor o valor solicitado
x = 0
while(x < 5): #bucle while
    print(x) #imprime valor o valor solicitado
    x += 1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value

print(person) #imprime valor o valor solicitado
person.pop('eye_color')#delete value
print(person) #imprime valor o valor solicitado

for topping in pizza_toppings: #bucle for
    if topping == 'Pepperoni': #Condicional
        continue
    print('After 1st if statement')
    if topping == 'Olives': #Condicional
        break #for loop

def print_hello_ten_times():
    for num in range(10): #bucle for
        print('Hello') #imprime valor o valor solicitado

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x): #bucle for
        print('Hello') #imprime valor o valor solicitado

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x): #bucle for
        print('Hello') #imprime valor o valor solicitado

print_hello_x_or_ten_times() #imprime valor o valor solicitado
print_hello_x_or_ten_times(4) #imprime valor o valor solicitado
 

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)