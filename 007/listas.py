# Listas

# equivalente a Arrays
# acepta distintos tipos de valores
# se expanden dinámicamente

nombre_lista = [1, "lista", True, 43.2332, [1,2,3]]
print(nombre_lista)

# Indices negativos -> empieza al revés, y -1 es el último, -2, el penúltimo, y así
print(nombre_lista[-2])

# Slicing
nombre_lista[0:3] # -> Incluye el elemento 0, y excluye el elemento 3

nombre_lista[:3] # -> al omitir el 0, py entiende que va desde el principio
nombre_lista[2:] # -> al igual con dejar vacío el final

nombre_lista[1:1] # -> devuelve una lista vacía

# Agregar elementos
nombre_lista.append('Rodri')
print(nombre_lista)

nombre_lista.insert(2, 'meses')
print(nombre_lista)

nombre_lista.extend(['otra', 'lista', 'nueva'])
print(nombre_lista)

# Buscar por índice
print(nombre_lista.index('Rodri')) # -> si no lo encuentra, lanza excepción
print(nombre_lista.index('lista')) # -> está más de una vez, devuelve la primera aparición

# Verificar si un elemento en la lista (devuelve True/False)
print('Carlos' in nombre_lista)
print('otra' in nombre_lista)

# Eliminar elementos
nombre_lista.remove('otra')
print(nombre_lista)

nombre_lista.pop() # Borra el último elemento

# Sumar listas
letras = ['a', 'b', 'c']
nums = [1,2,3]

unido = letras + nums
print(unido)

# Repetir listas
mi_lista = nombre_lista * 3
print(mi_lista)
