def suma(n1, n2):
    '''
    Suma dos números pasados por parámetro.

    Definición de pruebas:
    >>> suma(2,2)
    4

    >>> suma(2,2)
    4.0

    '''
    return n1+n2

print(suma(32, 44))

def es_mayor(n1, n2):
    '''
    >>> es_mayor(3, 1)
    False

    '''
    return n1 > n2



def maximo_valor(lista):
    '''
    # Sangrando el valor a ejecutar
    
    >>> lista1 = []
    >>> for i in [23, 43, 66, 5, 7565]:
    ...     lista1.append(i)
    >>> maximo_valor(lista1)
    7565

    # Verificando si se lanzan excepciones
    >>> maximo_valor(None)
    Traceback (most recent call last):
        ...
    TypeError: 'NoneType' object is not iterable


    
    '''
    return max(lista)





import doctest
doctest.testmod()