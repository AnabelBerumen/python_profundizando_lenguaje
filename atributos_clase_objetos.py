class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



# mostrar los atributos de un objeto

persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__)

# crear un atributo al vuelo
print(persona1.contador_personas) # atributo de clase
# pero solo se puede modificar con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
# el atributo anterior oculta al atributode clase
print(Persona.contador_personas)

persona2 = Persona('Karla', 'Gomez')
print(persona2.__dict__)