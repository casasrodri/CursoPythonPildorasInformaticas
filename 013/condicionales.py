# Operador and / or
peso = 80
altura = 1.75

if peso > 75 and altura < 2 or peso > 200:
    print("Estas gordito!")

# Operador in
colores = ['red', 'blue', 'dark']

print("Colores diponibles:")
print(colores)
fav = input("Elige tu color favorito: ")

if fav in colores:
    print("Buena elección!")
else:
    print('Color no disponible :(')
