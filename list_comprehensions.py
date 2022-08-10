numeros = range(10)
lista_pares = []

# creamos una nueva lista
for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero * numero)

print(lista_pares)

# list comprehensions
# [expresion for var in colection if condition]

lista_pares = []
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(lista_pares)

# ejemplo similar con dos condiciones
# divisible entre 2 y divisible entre 6

pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]
print(pares)

# if else
lista_pares = []
lista_inpares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_inpares.append(numero)

print(f'Pares {lista_pares}')
print(f'Impares: {lista_inpares}')

lista_pares = []
lista_inpares = []
[lista_pares.append(numero) if numero % 2 == 0 else lista_inpares.append(numero) for numero in range(10)]
print(f'Pares {lista_pares}')
print(f'Impares: {lista_inpares}')

# lista de listas
lista_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# convertimos la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'Lista simple {lista_simple}')

#  otro ejemplo
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor %2 == 0:
            lista_pares.append(valor)

print(f'Lista pares {lista_pares}')

# ahora con list comprehension
lista_pares = []
lista_pares = [valor for sublista in lista_listas for valor in sublista if valor %2 == 0]
print(f'List Comprehension{lista_pares}')
