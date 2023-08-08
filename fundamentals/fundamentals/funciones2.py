# #cuenta regresiva
def count_down(y):
     print(y)
     y -= 1
     if y >=0:
         count_down(y)
count_down(5)

print('------------------------------------------------')

#Imprimir y devolver
def imprimir_y_devolver(a,b):
    if a<b:
       print(a)
    elif b>a:
        return(b)
imprimir_y_devolver(1,2)

print('------------------------------------------------')

#Primero más longitud
num = [1,2,3,4,5]
def primero_mas_longitud(num):
    list = num[0] + len(num)
    print(list)
primero_mas_longitud(num) 

print('------------------------------------------------')

#valores mayores que el segundo
lista = [5,2,3,2,1,4]
def valores_mayores_que_el_segundo(lista):
    for x in lista:
        if x > lista[1]:
            print(x)
valores_mayores_que_el_segundo(lista)

print('------------------------------------------------')

# #Esta longitud, ese valor
def length_and_value(siz,val):
    lon = []
    for i in range(0, siz):
        lon.append(val)
    return lon

print(length_and_value(6,8))



     