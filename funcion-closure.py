# es una funcion que define a otra y la regresa

# funcion principal
def operacion1(a, b):
    # Definimos una funcion interna o anidada
    def sumar():
        return a + b

    # retornar la funcion
    return sumar


def operacion(a, b):
    return lambda: a + b


mi_funcion_closure = operacion(5, 2)
print(f'Resultado {mi_funcion_closure()}')

# llamar la funcion regresada al vuelo
print(f'Resultado al vuelo {operacion(2, 3)()}')
