'''
Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
'''
#Nombre completo: Darian Bellandi

#mi_lista = [7,10,5,-5,-1,8,4]

def promediando_enteros_positivos(lista:list)->float:
    '''Toma los números ingresados por lista y devuelve únicamente el promedio
        de la suma de los números positivos
    Args:
        lista(list): Lista de números enteros

    Returns:
        promedio (float):  promedio de números positivos
    '''
    promedio = 0
    cantidad_positivos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            promedio += lista[i]
            cantidad_positivos += 1
    promedio = promedio / cantidad_positivos
    return promedio

#print(promediando_enteros_positivos(mi_lista))