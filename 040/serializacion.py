from turtle import color


class Perro:
    def __init__(self, color, raza) -> None:
        self.color = color
        self.raza = raza

    def ladrar(self):
        print("Guau!")
    
    def __str__(self) -> str:
        return(f"El perrito es de raza {self.raza} y es de color {self.color}.")

luqui = Perro('gris', 'Yorkie')
print(luqui)

import pickle

file = open('040/perros', 'wb')
pickle.dump(luqui, file)
file.close()
del file


# Lectura
    # Previamente declarada la clase

file = open('040/perros', 'rb')
luquita = pickle.load(file)
file.close()
del file

print(luquita)