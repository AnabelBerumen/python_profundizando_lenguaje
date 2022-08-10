import math
from decimal import Decimal
# NaN - not a number
# NaN no es sensible a mayusculas o minusculas
# es un tipo de dato numerico valor indefinido
a = float('NaN')
print(f'a: {a}')
print(f'Es NaN? {math.isnan(a)}')

a = float('2.5')
print(f'a: {a}')
print(f'\nEs NaN? {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'\nEs NaN? {math.isnan(a)}')
