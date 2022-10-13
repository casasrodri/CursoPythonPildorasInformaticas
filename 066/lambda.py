# Funciones anónimas

'''
También llamadas:
on the go
on demand
online

'''
# Función común

def areaTriangulo(base, altura):
    return (base*altura)/2

print(areaTriangulo(5,7))


area_triang = lambda base, altura: (base*altura)/2

print(area_triang(5,7))

al_cubo = lambda num:pow(num, 3)

print(al_cubo(5))