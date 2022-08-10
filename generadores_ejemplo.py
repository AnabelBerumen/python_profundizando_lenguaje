def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecucion')


gen = generador_numeros()

for valor in gen:
    print(f'valor {valor}')

gen = generador_numeros()
print(f'Consumimos a demanda {next(gen)}')
print(f'Consumimos a demanda {next(gen)}')
print(f'Consumimos a demanda {next(gen)}')

# try except
try:
    print(f'Consumimos a demanda {next(gen)}')
    print(f'Consumimos a demanda {next(gen)}')
    print(f'Consumimos a demanda {next(gen)}')
    print(f'Consumimos a demanda {next(gen)}')
    print(f'Consumimos a demanda {next(gen)}')
except StopIteration as e:
    print(f'Ocurrio una excepcion {e}')

# while
while True:
    try:
        valor = next(gen)
        print(f'Impresion valor generador: {gen}')
    except StopIteration as e:
        print('Se termino de iterar el generador')
        break