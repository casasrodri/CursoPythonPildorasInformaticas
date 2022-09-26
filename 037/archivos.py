from io import open

# Modos:
# [r] lectura          
# [w] escritura
# [a] append

# Escritura
file = open('037/archivo.txt', 'w')
file.write("Hola, como estas?\nAdios")
file.close()

# Lectura
file = open('037/archivo.txt', 'r')
texto = file.read()
lineas = file.readlines()
file.close()

print(texto)

file = open('037/archivo.txt', 'r')
lineas = file.readlines()
file.close()

for i in lineas:
    print("--->", i)

print(lineas)

# Append
file = open('037/archivo.txt', 'a')
file.write("\nEl ultimo adios!")
file.close()
