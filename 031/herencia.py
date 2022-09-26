# super
# isintance()


class Persona():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def descripcion(self):
        print(f"Nombre: {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, sueldo) -> None:
        super().__init__(nombre)
        self.sueldo = sueldo

    def descripcion(self):
        super().descripcion()
        print(f"Sueldo: {self.sueldo}")


emp = Empleado('Rodri', 10032.0)
emp.descripcion()

print(isinstance(emp, Empleado))
print(isinstance(emp, Persona))