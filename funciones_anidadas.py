# funciones aninadadas
def calculadora(a, b, operacion ='sumar'):

    def sumar(a, b):
        return a + b



    def restar(a, b):
        return a - b

    if operacion == 'sumar':
        print(f'Resultado de la suma {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado de la resta {restar(a, b)}')


calculadora(5, 6)
calculadora(4, 3, 'restar')