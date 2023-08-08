#1
def número_de_grupos_alimentarios():
    return 5
print(número_de_grupos_alimentarios())
#retorna el valor de 5

#2
def número_de_ramas_militares():
    return 5
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo() + número_de_ramas_militares())
#imprime error por que no tiene comillas ('') y tampoco esta definido

#3
def número_de_libros_en_espera():
    return 5
    return 10
print(número_de_libros_en_espera())
#retorna el valor de 5

#4
def número_de_dedos():
    return 5
    print(10)
print(número_de_dedos())
#retorna el valor de 5

#5
def número_de_lagos_grandes():
    print(5)
x = número_de_lagos_grandes()
print(x)
#imprime 5 y none

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#es error porque esta print(linea 36) en ves de return

#7
def concatenar(b,c):
    return str(b)+str(c)
"función de soporte python from-rainbow">print(concatenar(2,5))
#imprime 25

#8
def número_de_océanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(número_de_oceános_o_dedos_o_continentes())
#retorna el valor 100, 10

#9
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3))
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))
#imprime 7, 14, 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#retorna el valor de 8

#11
b = 500
print(b)
def foobar():
    b ="operador de palabra clave from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)
#imprime el valor de 500, 500 

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#imprime 500, 500, 300, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#imprime 500, 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#imprime 1, 2, 3

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#imprime 1, 3, 5,











