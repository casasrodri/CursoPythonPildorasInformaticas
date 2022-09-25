# Generadores
# se extraen valor de una funcion, y se almacenan en un iterador
# se almacenan uno a uno, y queda en standby hasta que se solicte el siguiente

# vs. funcion tradicional
def numeros_pares():
    return (2,4,6,8,10)

# uso de la palabra reservada: yield

# Ventajas:
# - eficiencia

# Ejemplo
def generaPares(limite):
    num = 1
    lista = []

    while num<limite:
        lista.append(num*2)
        num += 1

    return lista

print(generaPares(10))

def generaPar(limite):
    num = 1
    while num<limite:
        yield num*2
        num += 1

# como se devuelve un obj iterable, lo tengo que guardar en una variable
devuelve_pares = generaPar(10)

for i in devuelve_pares:
    print(f"El valor asumido es: {i}")

print(type(devuelve_pares))

devuelve_pares = generaPar(10)

print(next(devuelve_pares))
print("Acá iría más código...")
print(next(devuelve_pares))
print("Acá iría más código...")
print(next(devuelve_pares))
