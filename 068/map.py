class Empleado:
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.nombre} - Sueldo: {self.sueldo}."

def calculo_comision(empleado):
    empleado.sueldo = empleado.sueldo * 1.03
    return empleado

empleados = [
    Empleado('Rodri', 5600),
    Empleado('Pedro', 3455),
    Empleado('Juan', 1433),
    Empleado('Chacho', 6005),
    Empleado('Luis', 4300),
]

listaComisiones = map(calculo_comision, empleados)

for empl in listaComisiones:
    print(empl)