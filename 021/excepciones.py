
num1 = 9
num2 = 0

try:
    division = num1/num2
except ZeroDivisionError:
    print("No se puede dividir por cero!")
    exit()


if division > 3:
    print('Es mayor a tres!')
else:
    print('No es mayor a tres!')

print('Fin del programa')
