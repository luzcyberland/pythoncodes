#[5,1,3,2,4]
def suma(lista):
    ''' funcion que calcula la sumatoria de una lista'''
    aux = lista[0]
    com = 0
    for i in lista:
        suma= aux + com
        aux = suma
        com = i
    return suma


lista = [4,4,4,4,4]
print(suma(lista))


