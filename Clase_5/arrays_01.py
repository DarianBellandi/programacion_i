'''
Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
'''
#Nombre completo: Darian Bellandi


mi_lista = [7,10,5,8,4]

def promediando_enteros(lista:list)->float:
    '''Toma los números ingresados por lista y devuelve el promedio
        de la suma de todos los números
    Args:
        lista(list): Lista de números enteros

    Returns:
        promedio (float):  
    '''
    promedio = 0
    for i in range(len(lista)):
        promedio += lista[i]
    promedio = promedio / len(lista)
    return promedio

#print(promediando_enteros(mi_lista))