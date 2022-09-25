# continue:
    # Pasa a la siguiente iteración

from turtle import end_fill


for c in "Python":
    if c == 'h':
        continue
    print(c)

# pass:
    # devuelve null cuando se está ejecutando el bucle, es "como si no se ejecutara"
    # (por ejemplo para clase nula o bucle pendiente de desarrollar)
#while True:
#    pass

#class MiClase:
#    pass # para implementar más tarde

# else:
    # se ejecuta siempre que se ejecute la ultima iteración, si hay un break, se saltea el 'else'

for i in "Rodri":
    print(i)
else:
    print("adios")
