class Auto():
    largo_chasis = 250
    ancho_chasis = 120
    en_marcha = False
    __volante = 1  # 2 guiones bajos la convierten en variable privada (para lectura o escritura)

    def __init__(self):
        self.ruedas = 6

    def arrancar(self):
        self.en_marcha = True
    
    def estado(self):
        if self.en_marcha:
            return "El auto está andando."
        else:
            return "El auto está estacionado."

    def __metodo_encapsulado(self):
        pass

autito = Auto()
print(autito.ruedas)
print(autito.estado())
autito.arrancar()
print(autito.estado())

print(autito.__volante)