# Tuplas

# son inmutables, no se puede modificar luego de la creación
# permiten: slicing, comprobar si un elemento en la lista

# pueden usarse como claves de un diccionario, las listas no

tupla = (1, 3, 'ewe')

# Convertir en lista
lista = list(tupla)
print(type(lista))

# Convertir lista en tupla
lista = [23, 325, 5454, 23]
tuplaa = tuple(lista)
print(tuplaa)

# Verificar si un elemento en tupla
print(3 in tuplaa)

# Contar elementos
print(tuplaa.count(23))

# Saber la longitud
print(len(tuplaa))

# Crear tupla unitaria
unit = (2323, )  #* Si o Si debe ponerse esta coma para que funcione así

# Empaquetado de tupla
tupla_sin_parentesis = 23, ' rweod', 2323.442   #! NO recomendado
print(type(tupla_sin_parentesis))

# Desempaquetado de tupla
tupla = (23, 3455, 644 ,'2323')
ano, mes, dia, hora = tupla
print(mes)
    # Lanza excepción si no coincide la cantidad de elementos y variables


