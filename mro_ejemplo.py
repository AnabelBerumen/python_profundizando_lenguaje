class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Metodo clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase2')
        super().metodo()


class Clase3(Clase1):
    def __init__(self):
        print('Clase 3.__init__')
        super().__init__()


    def metodo(self):
        print('Metodo clase3')
        super().metodo()


class Clase4(Clase2, Clase3):
    def metodo(self):
        print('Metodo clase4')
        super().metodo()


clase4 = Clase4()

# saber la clase padre
print(Clase4.__base__)
# mro
print(Clase4.__mro__)

clase4.metodo()