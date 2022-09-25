# Generadores

# YIELD FROM
# se usa para simplicar en el caso de usar bucles anidados

def devuelve_ciudades(*ciudades): # El * del argumento, denota un num indeterminado de argumentos (en tupla)
    for elem in ciudades:
        #for subelem in elem:
            yield from elem

ciudades_devueltas= devuelve_ciudades('Córdoba', 'Buenos Aires', 'Bariloche', 'Rosario')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
