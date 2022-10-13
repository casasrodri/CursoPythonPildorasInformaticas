import re

# metacaracteres

lista = [
    'Rodri Casas',
    'Pedro Rodriguez',
    'Camila Aldao',
    'Rocio Fernandez',
    'Agustin Vieroschi'
]

print('\nEstá al principio:')
for e in lista:
    if re.findall('^Rodri', e): # Si la palabra está al comienzo
        print('\t - {}'.format(e))

print('\nEstá al final:')
for e in lista:
    if re.findall('ez$', e): # Si la palabra está al final
        print('\t - {}'.format(e))

print('\nContiene alguno:')
for e in lista:
    if re.findall('[aV]', e): # Si la palabra contiene alguno de ellos
        print('\t - {}'.format(e))