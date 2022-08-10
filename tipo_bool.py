# tipo numeric falso 0, true lo otro
valor = 0
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = 12
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

# tipo str false "" true lo otro
valor = 'hola'
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

# tipo colecciones. False = vaciás, True todo lo otro
# listas
valor = []
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

valor = [1, 2, 3]
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

# tuplas
valor = ()
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

valor = (1, 2, 3)
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

# diccionario
valor = {}
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

valor = {'a': 1, 'b': 2}
resultado = bool(valor)
print(f'\nValor {valor}, resultado: {resultado}')

if not '':
    print('Return False')
else:
    print('Return True')

if '':
    print('Return True')
else:
    print('Return False')

variable = ''

if bool(variable):
    print('Return True')
else:
    print('Return False')

if variable:
    print('Return True')
else:
    print('Return False')

while variable:
    print('ciclo while')
else:
    print('fin')
