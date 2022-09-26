class Perro:
    def hacer_ruido(self):
        print("Guau!")

class Gato:
    def hacer_ruido(self):
        print("Miau!")

zoo = [Perro(), Gato()]


def no_silencio(animal):
    animal.hacer_ruido()
    
for animal in zoo:
    no_silencio(animal)
