
def decoradora(fx):
    def funcion_interna():
        print('El resultado del cálculo es:')
        fx()
        print('Se finalizó con el cálculo.\n\n')
    return funcion_interna



@decoradora
def suma():
    print(3+2)


@decoradora
def resta():
    print(3-2)



suma()
resta()