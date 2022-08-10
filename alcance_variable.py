# alcance de variables(scope)

var_global = 'Variable global'

def imprimir():
    print(f'Variable global desde funcion: {var_global}')

    var_local = 'Variable local'
    print(f'Variable local desde funcion: {var_local}')


imprimir()
print(f'Variable global fuera de la funcion: {var_global}')
