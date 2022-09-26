import pickle

class ArchivoExterno:
    def __init__(self) -> None:
        self.__path = '041/binario'

    def save(self, obj):
        pickle.dump(obj, open(self.__path, 'wb'))

    def load(self):
        return pickle.load(open(self.__path, 'rb'))

class Persona:

    externo = ArchivoExterno()
    
    def __init__(self, nombre, apellido) -> None:
        self._nombre = nombre
        self.apellido = apellido
            
    def __str__(self) -> str:
        return "{} {}".format(self._nombre, self.apellido)

    # Getter NOMBRE
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, name):
        self._nombre = name
        self.externo.save(self)

    def recuperar_bin(self):
        print("Lectura del archivo recuperado:")
        print(self.externo.load())  # type: ignore



rodri = Persona('Rodri', 'Casas')
print(rodri)

rodri.nombre = 'Rodrigo'
print(rodri)

rodri.recuperar_bin()

rodri.nombre = 'Adrián Rodrigo'
rodri.recuperar_bin()