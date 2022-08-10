class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, item):
        return self._elementos[item]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__} {self._elementos!r}'


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)

        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordenar()


class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)

        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)


# lista de enteros ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)

lista_ordenada = ListaOrdenada([4, 8, 5, 7, 5, 8])
print(lista_ordenada)

lista_enteros = ListaEnteros([3, 4, 6])
print(lista_enteros)

enteros_ordenada = ListaEnterosOrdenada([2, 7, 4, 9, 2, 6])
print(enteros_ordenada)

# saber el orden de las clases
print(ListaEnterosOrdenada.__bases__)
print(ListaEnterosOrdenada.__mro__)

# isinstance
print('Es entero', isinstance(10, int))
print('Es cadena', isinstance('sdsds', str))
print('Es lista entero ordenado?', isinstance(enteros_ordenada, ListaOrdenada))
print('Es lista de enteros?', isinstance(enteros_ordenada, ListaEnteros))
print('Es varios tipos?', isinstance(enteros_ordenada, (ListaEnterosOrdenada, ListaEnteros)))

