class Vehiculo():
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.en_marcha = False
    
    def arrancar(self):
        self.en_marcha = True
    
    def estado(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - En marcha?: {self.en_marcha}")

class Moto(Vehiculo):
    willy = False
    def hacer_willy(self):
        self.willy = True
        print("Voy haciendo willy :D")
    
    # Haciendo override del método original
    def estado(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - En marcha?: {self.en_marcha} - Willy: {self.willy}")

moto = Moto()
moto.marca = 'Honda'
moto.modelo = 2022
moto.estado()
moto.hacer_willy()
moto.estado()