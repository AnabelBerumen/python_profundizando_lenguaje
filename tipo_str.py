# profundizando en el tipo str

# concatenacion automatica en pyhon
import math

msj = 'hola' 'mundo'
print(msj)
variable = 'wiw'
msj = 'hola' 'mundo' + variable
print(msj)

help(str.capitalize)

help(math)
nombre = 'anabel'
edad = 32
sueldo = 50000

msj = ' Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(msj)

msj = 'Nombre {n} Edad{e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(msj)

diccionario = {'nombre': 'ivan', 'edad': 34, 'sueldo': 100000}
mensaje = 'Nombre {dic[nombre]}'.format(dic=diccionario)
print(mensaje)

res = 5 * ('hola', 10)
print(f'Resultado {res}')

res = 10*[0]
print(f'Resultado {res} largo {len(res)}')

