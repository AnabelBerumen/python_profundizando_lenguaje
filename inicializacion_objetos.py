# Orden de inicializacion de objetos
class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo padre')


class Hijo(Padre):

    def __init__(self):
        super().__init__()
        print('Inicializando hijo')

    def metodo(self):
        super().metodo()
        print('Metodo sobrescrito de la clase hija')


print('====PADRE====')
padre1 = Padre()
padre1.metodo()

print('=====HIJO====')
hijo1 = Hijo()
hijo1.metodo()
