class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_valores(cls, nombre, apellido):
        return cls(nombre, apellido)
    def __str__(self):
        return f'Nombre {self.nombre}, Apellido {self.apellido}'


persona1 = Persona('Juan', 'Perez')
persona_vacio = Persona.crear_persona_vacia()
persona_valores = Persona.crear_persona_valores('Karina','aguallo')
print(persona1)
print(persona_vacio)
print(persona_valores)