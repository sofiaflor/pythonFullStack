def numeros():
    lista = []
    for i in range (1, 256):
       lista.append(i)
    return lista
var = numeros()
print(var)

def sumarnumeros(lista):
    sun =  sum(lista)
    return sun
    
arr = [2,3,4,5] 
var = sumarnumeros(arr)
print(var)

def multiple(arr):
    sum = 0
    for i in range (len(arr)):
        sum = sum + arr[i]
    return sum/len(arr)

sun =[1,3,5,7,20]
var = multiple(sun)
print(var)



       
    

