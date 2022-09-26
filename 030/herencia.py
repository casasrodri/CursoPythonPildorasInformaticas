# Herencia múltiple

class Animal:
    def __init__(self, raza, color) -> None:
        self.raza = raza
        self.color = color

    def inspect(self):
        print(f"Raza: {self.raza} - Color: {self.color}")

class Perro(Animal):
    pass

perrito = Perro('Yorkie', 'Gris')
perrito.inspect()

class Volador():
    cantidad_alas = 0
    def __init__(self, pico) -> None:
        self.pico = pico

    def inspect(self):
        print(f"Cantidad de alas: {self.cantidad_alas}")

    def graznar(self):
        print("Cuak!")

class Pato(Animal,Volador):
    pass
    # Tanto el constructor como los métodos, serán tomados de la primera clase mencionada.


pato = Pato('Duck', 'Blanco')
pato.inspect()
pato.graznar()