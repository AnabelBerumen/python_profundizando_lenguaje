# funciones anonimas
def sumar(a, b):
    return a + b


mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(4,6)

print(f'Resultado lambda {resultado}')


# funcion lambda que no recibe argumentos
mi_funcion_lambda = lambda : 'Funcion sin argumentos'
print(f'Funcion lambda sin argumentos {mi_funcion_lambda()}')

# funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Argumentos por default {mi_funcion_lambda()}')
print(f'Argumentos por default {mi_funcion_lambda(4,9)}')

# funcion lambda con argumentos variables *args y *kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(f'Res argumentos variables: {mi_funcion_lambda(1,2,3, a=5, b=2)}')

# Funciones lambda con argumentos variables y valores por default

mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado lambda: {mi_funcion_lambda(1,2,3,5,6,7,e=5,t=6)}')