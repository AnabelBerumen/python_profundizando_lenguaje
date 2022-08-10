# diccionarios guardan un orden

dic = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 34}
print(dic)

# los dic son mutables, pero las llabes deben ser inmurables
# dic = {[1,2]: 'Valor1"}

# dic ={(1, 2): 'valor1'}
print(dic)

dic['Departamentos'] = 'Sistemas'
print(dic)

# no hay valores duplicados en las llaves de un diccionario
print(dic['Nombre'])

# metodo get recupera una lave

print(dic.get('Nombre', 'No se encontro la llave'))
print(dic.get('Nombres', 'No se encontro la llave'))

# setdeault si modifica el diccionario
nombre = dic.setdefault('Nombre', 'Valor por default')
print(dic)
nombre = dic.setdefault('Nombres', 'Valor por default')
print(dic)

# imprimir pprint
from pprint import pprint as pp
# help(pp)
pp(dic, sort_dicts=False)