'''
Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
'''
#Nombre completo: Darian Bellandi



def multiplicando_enteros(lista:list)->float:
    '''Toma los números ingresados por lista y devuelve el promedio
        de la multiplicación de todos los números
    Args:
        lista(list): Lista de números enteros

    Returns:
        promedio (float): promedio del producto de todos los números
    '''
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion


#mi_lista = [7,10,5]
#print(multiplicando_enteros(mi_lista))