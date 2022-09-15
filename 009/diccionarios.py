# Diccionarios

from filecmp import dircmp


dict = {'nombre': 'Rodri', 'apellido': 'casas', 'edad': 30}
print(dict['nombre'])

# Agregar elementos
dict['altura'] = 1.7
print(dict)

# Eliminar
del dict['apellido']
print(dict)

# Usando tuplas
tupla = ('Francia', 'España', 'Reino Unido') # parece que tambien puede ser listas
mi_diccionario = {
    tupla[0]: 'París',
    tupla[1]: 'Madrid',
    tupla[2]: 'Londres'
}
print(mi_diccionario)
