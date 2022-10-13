import re

cadena = 'Vamos a aprender expresiones regulares en Python. Y aprender algo más en Python.'

# search() -> localiza donde está la regexp (sólo la primera vez que lo encontró)

regexp = 'aprender' 
# case-sensitive
# Devuelve None cuando no lo encuentra

print(re.search(regexp, cadena)) 

if re.search(regexp, cadena):
    print('Hemos encontrado el texto')
else:
    print('No se encontró el texto.')


textoEncontrado = re.search(regexp, cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())



# findall()
regexp = 'Python'
print(re.findall(regexp, cadena)) 
print(f'La palabra {regexp} se encontró {len(re.findall(regexp, cadena))} veces.')

