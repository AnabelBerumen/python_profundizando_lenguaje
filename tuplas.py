# Tuplas inmutables
a, b = 'Hola', 'Adios'
print(a, b)
# swap intercambio
a, b = b, a
print(a, b)


def minmax(elementos):
    return min(elementos), max(elementos)


min, max = minmax([1, 3, 4, 6, 8])

print(f'Valor min: {min}, Valor max: {max}')

# regresar la suma de una tupla
resultado = sum((1, 2, 3, 4, 5))
print(resultado)


def sumar(*args):
    return sum(args)


resultado = sumar(1, 2, 4, 6, 8)
print(f'Resultado {resultado}')

