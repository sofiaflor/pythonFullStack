# 1Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
x[1] [0] = 15
print(x)

print('------------------------------------------')

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0] = {'first_name':  'Michael', 'last_name' : 'Bryant'}
print(estudiantes[0])

print('------------------------------------------')

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'] = ['Andres', 'Ronaldo', 'Rooney']
print(directorio_deportes)

print('------------------------------------------')

z = [ {'x': 10, 'y': 20} ]
z = [{'x': 10, 'y': 30}]
print(z)

#2Iterar a través de una lista de diccionarios


estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(lista):
    for i in range(0,len(lista)):
        salida =""
        for clave, valor in lista[i].items():
            salida += f"{clave} - {valor} ,"
            print(salida)
iterateDictionary(estudiantes)

#3 Obtener valores de una lista de diccionarios
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(nombre_clave, lista):
    for diccionario in lista:
        print(diccionario[nombre_clave])

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name',estudiantes)


#4.-Iterar a través de un diccionarios con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
 }

def imprimir_info(diccionario):
    for clave, valor in diccionario.items():
        print("*********************")
        print(f"{len(valor)} {clave.upper()}")
        
        for i in range(0,len(valor)):
            print(valor[i])



imprimir_info(dojo)