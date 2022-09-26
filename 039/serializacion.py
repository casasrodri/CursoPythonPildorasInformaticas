import pickle as pk

nombres = ['Pau', 'Rodri', 'Luqui']

# Guardado

bin_file = open('039/binario_lista','wb') # Write Binary

pk.dump(nombres, bin_file)
bin_file.close()

del bin_file

# Recuperado

archivo = open('039/binario_lista','rb') # Read Binary
lista = pk.load(archivo)

print(lista)