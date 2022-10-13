import re

# metacaracteres

lista = [
    'Rodri Casas',
    'Pedro Rodriguez',
    'Camila Aldao',
    'Rocio Fernandez',
    'Agustin Vieroschi',
    'Ro021',
    'Ro02',
    'Ro1',
    'Ro2'
]

print('\nRango de letras:')
for e in lista:
    if re.findall('[t-xQ-Y]', e): # Si la palabra está al comienzo
        print('\t - {}'.format(e))

print('\nRango de números:')
for e in lista:
    if re.findall('Ro[0-1]', e): # Si la palabra está al final
        print('\t - {}'.format(e))
