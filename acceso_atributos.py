# ejemplo atributos publicos, protegidos y privados

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido # solo en esta clase y subclases
        self.__privado = privado # no se modifica, solo en esta clase se usa, no subclase


object = MiClase('Publico', 'Protegido', 'Privado')

print(object.publico)
object.publico = 'nuevo valor Publico'
print(object.publico)


print(object._MiClase__privado)
object._MiClase__privado = 'Nuevo valor privado'
print(object._MiClase__privado)