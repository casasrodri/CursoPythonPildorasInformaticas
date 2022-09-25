# Condicionales

def valoracion(nota):
    if nota <= 4:
        return "Desaprobado"
    else:
        return "Aprobado"

print(valoracion(5))
print(valoracion(4))

# Ejemplo pidiendo la nota por consola
print("Calificaciones de fin de año:")
nota = int(input("Introduce tu nota: "))
print("Tu calificación es:", valoracion(nota))


# Operadores ternarios
tern = "Me van a retar" if valoracion(4) == "Desaprobado" else "Todo ok"
print(tern)

    # No muy utilizada ni querida
tern = ("Todo oks","Me van a retarr")[valoracion(4) == "Desaprobado"]
print(tern)

