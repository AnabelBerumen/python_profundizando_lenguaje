multiplicacion = (valor * valor for valor in range(4))
print(type(multiplicacion))
print(multiplicacion)
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# pasarl oa una funcion
import math

suma = sum(valor * valor for valor in range(4))
print(f'Resultado de la suma {suma}')

# tambien podemos usar una lista
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(next(generador))

lista = ['Karla', 'Gomez']
contador = 0


def incrementar():
    global contador
    contador += 1
    return contador


generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(cadena)