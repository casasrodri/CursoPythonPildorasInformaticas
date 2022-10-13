
def decoradora(fx):
    def funcion_interna(*args, **kwargs):
        # *args         representa un número indeterminado de parámetros
        # **kwargs      representa un número indeterminado de parámetros (con keywords)
        print('El resultado del cálculo es:')
        fx(*args, **kwargs)
        print('Se finalizó con el cálculo.\n\n')
    return funcion_interna

def modifico_parametros(fx):
    def menos_uno(b,p):
        b = b-1
        p = p-1
        fx(b,p)
    return menos_uno

@decoradora
@modifico_parametros
def suma(n1,n2):
    print(n1+n2)


@decoradora
def resta(n1,n2):
    print(n1-n2)

@decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(4, 8)
resta(235, 674)

potencia(base=5,exponente=3)