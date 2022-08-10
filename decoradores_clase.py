import inspect


def decorador_repr(cls):
    print('Se ejecuta el decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # revisar atributos de la clase con el metodo vars
    atributos = vars(cls)
    for nombre, atributo in atributos.items():
        print(nombre, atributo)

    # revisar  si se sobrescribio el __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobrescrito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma metodo __init__: {firma_init}')

    # recuperamos lso parametros
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros init {parametros_init}')

    for parametro in parametros_init:
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para el parametro {parametro}')

    # crear el metodo repr dinamicamente
    def metodo_repr(self):
        return f'Resultado del metodo repr'

    # agregar dinamicamente
    setattr(cls, '__repr__', metodo_repr)
    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print('Se ejecuta el inicializador de clase Persona')
        self._nombre = nombre
        self._apellido = apellido


    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido


p1 = Persona('Juan', 'Perez')
print(p1)


