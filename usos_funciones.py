# First class citizens

def sumar(a, b):
    return a + b


# asignar una funcion a una variable(no se usan parentesis)

mi_funcion = sumar

print(type(mi_funcion))
resultado = mi_funcion(5, 8)
print(resultado)

def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar {sumar_arg(a, b)}')


operacion(4, 5, mi_funcion)

# retornar funcion
def retornar_funcion():
    return sumar

mi_funcion_retornada = retornar_funcion()

print(f'Resultado de la funcion retornada: {mi_funcion_retornada(5, 7)}')