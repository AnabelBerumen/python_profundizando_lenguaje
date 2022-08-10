# print(dir(__builtins__))
# help(zip)

numeros = [1, 2, 3]
letras = 'a b c'.split()
identificadores = 321, 322, 323, 324, 324
conjunto = {6, 4, 0, 9, 8, 15, 10}
mezcla = zip(numeros, letras, identificadores, conjunto)
print(mezcla)
print(list(mezcla))
print(tuple(zip(numeros, letras)))
print(type(mezcla))

# iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores,conjunto):
    print(f'Numero {numero}, Letra: {letra}, ID: {id}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores,conjunto):
    nueva_lista.append(f'{id}-{numero}-{id}-{aleatorio}')

print(nueva_lista)

# unzip
mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*mezcla)
print(numeros)
print(letras)

# ordenamiento usando zip
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 2, 4, 1, 0]
mezcla = zip(letras, numeros)
print(tuple(mezcla))

# ordenamiento
print(sorted(zip(letras, numeros)))
print(sorted(zip(numeros, letras)))

llaves = ['Nombre', 'Apellido', 'Edad']
valor = ['Juan', 'Perez', 19]
diccionario = dict(zip(llaves, valor))
print(diccionario)

# actualizar un elemento del diccionario

llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)