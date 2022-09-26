from io import open
import os.path

path = os.path.dirname(__file__) + '/../037/archivo.txt'

file = open(path, 'r')
print(file.read())

# la siguiente linea no imprime nada, porque el puntero se fue al final del archivo
print(file.read())

# Uso del cursor
file.seek(0)
print(file.read())

file.seek(8)
print(file.read())

# Si se quiere leer los 10 primeros caracteres

file.seek(0)
print("10 primeros caracteres:")
print(file.read(10))
print("Resto de caracteres:")
print(file.read())

file.close()

# Leer en modo simultaneo
file = open(path, 'r+') # Lectura y Escritura

lineas_actual = file.readlines()

lineas_actual[1] = "Cambio esta linea\n"

file.seek(0)
file.writelines(lineas_actual)
file.close()