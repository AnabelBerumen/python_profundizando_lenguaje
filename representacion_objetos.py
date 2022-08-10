# print(dir(object))
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # enfoque a programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre: {self.nombre}, apellido:{self.apellido})'

    # enfoque al usuario final u otro sistema
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

    
p1 = Persona('Juan', 'Perez')

print(p1)
print(f'Mi objeto p1: {p1!r}')
print(f'{p1}')