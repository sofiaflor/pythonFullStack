# 1.- Operaciones Matematicas
num = 10
num1 = num % 2
print(num1)
if num % 2 == 0:
    print("num es par")
   
else:
    print("num es impar")

x = 1
c = 0
while x <= num:
    if num % x == 0:
        c = c + 1
    x = x + 1
if c == 2:
    print("mun",num,"es primo")
else:
    print("num",num,"no es primo")        


# 2.- Arreglos
array = [
  [12,16,10],
  [7,34,37],
  [20,22,24]
]

i=0

while i < len(array):
    subArrays = array[i]
    print(subArrays[i])
    i +=1


matriz = array
print(matriz)
