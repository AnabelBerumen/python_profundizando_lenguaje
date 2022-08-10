# coleccion de elementos unicos y es mutable
# los elementos de un set deben ser inmutables

conjunto = {'alho', True, 18.0}

# set vacio
conjunto = set()
print(conjunto)
print(type(conjunto))

# mutable
conjunto.add('Juan')
print(conjunto)

# contenido unico
conjunto.add('Juan')
print(conjunto)

# crear a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)

# podemos agregar mas elementos o un set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)

conjunto.update([20, 30, 30, 30, 40 ,50 ])
print(conjunto)

# copia de un set poco profunda
conjunto_copia = conjunto.copy()
print(conjunto_copia)
print(f'Es igual al contenido {conjunto == conjunto_copia}')
print(f'Es la misma referencia {conjunto is conjunto_copia}')

# operaciones de conjuntos con set
# personas con distintas caracteristicas
pelo_negro = {'juan', 'karla', 'pedro', 'maria'}
pelo_rubio = {'lorenzo', 'laura', 'marco'}
ojos_cafe = {'karla', 'laura'}
menores_30 = {'juan', 'karla', 'maria'}

print(ojos_cafe.union(pelo_rubio))

# interseccion
print(ojos_cafe.intersection(pelo_rubio))

# diference a pero no en b
print(pelo_negro.difference(ojos_cafe))

# diferencia simetrica
print(pelo_negro.symmetric_difference(ojos_cafe))

# preguntar si un set esta contenido en otro a esta en b?
print(menores_30.issubset(pelo_negro))

#  a contiene a b (b esta en a)
print(menores_30.issuperset(pelo_negro))

# a no en b
print(pelo_negro.isdisjoint(pelo_rubio))
