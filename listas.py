nombres1 = ['juan', 'karla', 'pedro']
nombres2 = 'laura maria gonzalo ernesto'.split()

# sumar listas
print(nombres1 + nombres2)

# extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender lista1 con lista2 {nombres1}')

# lista de numeros
num1 = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original {num1}')
# obtener el indice del primer elemento encontrado en una lista
print(f'Indicie 4:  {num1.index(4)}')

# invertir los elementos de la lista
num1.reverse()
print(f'Lista invertida {num1}')

# ordenarlos de manera ascendente
num1.sort()
print(f'Lista ordenada {num1}')

# ordenar de manera descendente
num1.sort(reverse=True)
print(f'Lista ordenada descendente {num1}')

# obtener valor minimo y maximo
print(f'Valor minimo {min(num1)}')
print(f'Valor maximo {max(num1)}')

# copiar los elementos de una lista
num2 = num1.copy()
print(num1)
print(num2)
print(f'Misma referencia entre las listas {num1 is num2}')
print(f'Mismo contenido? {num1 == num2}')

# utilizar constructor de la lista
num2 = list(num1)
print(f'Misma referencia entre las listas {num1 is num2}')
print(f'Mismo contenido? {num1 == num2}')

# slicing
num2 = num1[:]
print(f'Misma referencia entre las listas {num1 is num2}')
print(f'Mismo contenido? {num1 == num2}')

# multiplicacion de listas
lista_multiplicada = 5*[[2,5]]
print(lista_multiplicada)
print(f'Misma referencia {lista_multiplicada[0] is lista_multiplicada[1]}')
print(f'Mismo contenido {lista_multiplicada[0] == lista_multiplicada[1]}')
lista_multiplicada[2].append(10)
print(lista_multiplicada)

# matrices
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(matriz)
print(f'F[0] C[0] {matriz[0][0]}')
print(f'F[2] C[3] {matriz[2][3]}')

lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
lista_listas.sort(key=len)
print(f'Ordenar lista {lista_listas}')

# build-in sorted
nombres1 = 'juan carlos pedro carla esperanza'.split()
nombres1 = sorted(nombres1)
print(nombres1)

nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

# ordenar por cantidad de caracteres
nombres1 = sorted(nombres1, key=len)
print(nombres1)

# built-in tipo reversed
nombres1 = reversed(nombres1)
print(nombres1)
print(list(nombres1))




