def perimCuadrado(lado):

        '''
        Calcula el perímetro de un cuadrado según el largo de los lados del cuadrado.
        '''

        return lado*lado


class Areas:

    '''
    Clase que realiza cálculos asociados a distintas formas geométricas.
    '''

    def areaCuadrado(lado):

        '''
        Calcula el área de un cuadrado según el largo de los lados del cuadrado.
        '''

        return lado*lado

    def areaTriangulo(base, altura):

        '''
        Calcula el área de un triángulo según la base y la altura del mismo!
        '''

        return (base*altura)/2

print('\n\n-----------------------------------')
print(perimCuadrado.__doc__)
print('-----------------------------------\n\n')

print('\n\n-----------------------------------')
help(perimCuadrado)
print('-----------------------------------\n\n')

print('\n\n-----------------------------------')
help(Areas.areaCuadrado)
print('-----------------------------------\n\n')

print('\n\n-----------------------------------')
help(Areas)
print('-----------------------------------\n\n')


from matematicas import basicas as matem

print(matem.sumar(100, 340))

print('\n\n-----------------------------------')
help(matem)
print('-----------------------------------\n\n')