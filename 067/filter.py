def numero_par(num):
    return num % 2 == 0

numeros = [12, 42, 65, 46, 775, 67, 65, 764, 72, 51, 60]

print(list(filter(numero_par, numeros)))

# Numeros impares usando lambda

print(list(filter(lambda num: num % 2 != 0, numeros)))


class Empleado:
    def __init__(self, nombre, area) -> None:
        self.nombre = nombre
        self.area = area

    def __str__(self) -> str:
        #return f"Nombre: {self.nombre} | Gerencia: {self.area}"
        return "Nombre: {} | Gerencia: {}".format(self.nombre, self.area)

empleados = [
    Empleado('Rodri', 'Auditoria'),
    Empleado('Pedro', 'Pagos'),
    Empleado('Juan', 'Tecnología'),
    Empleado('Chacho', 'Auditoria'),
    Empleado('Luis', 'Auditoria'),
]

print('Empleados de auditoría:')
for empleado in filter(lambda emp: emp.area == 'Auditoria', empleados):
    print(empleado)
