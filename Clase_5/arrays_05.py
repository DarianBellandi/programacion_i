'''
Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
'''
lista = [0,105,0,105,5,1,105,61,3,7,105]



def posicinar_maximo(lista:list)->list:
    '''Toma los números de una lista aleatoria y devuelve
    otra lista con todas las posiciones donde se encontró
    el número más grande

    Args:
        lista(list): Lista con números enteros aleatorios
    
    Returns:
        lista_posiciones(list): Lista las posiciones del número máximo
    '''
    maximo = lista[0]
    contador = 0
    for e in lista:
        if e > maximo:
            maximo = e
            contador = 1
        else:
            if e == maximo:
                contador += 1
    
    lista_posiciones = [0] * contador
    for i in range(len(lista)):
        if lista[i] == maximo:
            for j in range(len(lista_posiciones)):
                if lista_posiciones[j] == 0:
                    lista_posiciones[j] = i+1
                    break


        
        
    
    print(f"El número máximo ({maximo}) se encontró:\n")
    for i in lista_posiciones:
        print(f"\tEn la posición {i}")
    
    return lista_posiciones


posicinar_maximo(lista)