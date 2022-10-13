import re

# metacaracteres

lista = [
    'Rodri Casas',
    'Pedro Rodriguez',
    'Camila Aldao',
    'Rocio Fernandez',
    'Agustin Vieroschi',
    'Ro021',
    'rodrigo casas',
    'Ro02',
    'Ro1',
    'Ro2',
    'Lara Videla',
    'Mara Yamila',
    '349s0s9d0d90s9d',
    'ssa320392090923023'
]

print('\nTodos los Rodri:')
for e in lista:
    if re.search('Rodri', e):
        print(e)

# match()
# Busca desde el comienzo del texto
print('\nUsando match:')
for e in lista:
    if re.match('Rodri', e, re.IGNORECASE):
        print(e)

# El punto sustituye a un único caracter.

print('\nUsando el punto:')
for e in lista:
    if re.match('.Ara', e, re.IGNORECASE):
        print(e)

print('\nEmpieza con número:')
for e in lista:
    if re.match('\d', e, re.IGNORECASE):
        print(e)

