# extender funcionalidad

# 1.Funcion decorador (a)
# 2.Funcion a decorador (b)
# 3.Funcion decoradora (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Funcion C --antes--')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Funcion B --despues--')
        return resultado
    return funcion_decorada_c



@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde funcion mostrar_mensaje')

@funcion_decorador_a
def imprimir():
    print('Imprimir')

mostrar_mensaje()
print('-----ESPACIO-----')
imprimir()
print('-----ESPACIO-----')
@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(5, 6)
print(resultado)