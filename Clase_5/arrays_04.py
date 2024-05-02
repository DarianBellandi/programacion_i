'''
Escribir una función que reciba como parámetros una lista de enteros y retorne
la posición del valor máximo encontrado.
'''
#Nombre completo: Darian Bellandi

#mi_lista = [7,10,5,-5,-1,8,2]

def posicionar_valor_maximo(lista:list)->int|None:
    '''Toma los números ingresados por lista y devuelve la posición del valor 
    máximo.

    Args:
        lista(list): Lista de números enteros

    Returns:
        posicio(int): posición del valor máximo
    '''
    flag_maximo = True
    for i in range(len(lista)):
        if lista[i] > 0:
            if flag_maximo == True:
                maximo = lista[i]
                posicion = i
                flag_maximo = False
            else:
                if maximo < lista[i]:
                    maximo = lista[i]
                    posicion = i
    return posicion

#print(posicionar_valor_maximo(mi_lista))


