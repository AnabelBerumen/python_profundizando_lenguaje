# Generadores
# es una funcion especial en python

def generador():
    yield 1
    yield 2
    yield 3


# consumimos el generador
gen = generador()
# con cada llamada consumimos el valor
print(next(gen))
print(next(gen))
print(next(gen))


for valor in generador():
    print(f'Numero generado: {valor}')