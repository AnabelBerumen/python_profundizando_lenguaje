def funcion_externa():
    variable_local_externa = 'Variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        nonlocal variable_local_externa
        variable_local_externa = 'nuevo valor variable local externa'

    funcion_anidada()

    print(f'Valor variable local externa: {variable_local_externa}')


funcion_externa()

contador = 0


def mostrar_contador():
    print(contador)


def modificar_contador(c):
    global  contador
    contador = c


modificar_contador(5)
mostrar_contador()
