'''
Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
'''
lista = [0,105,0,105,5,1,105,61,3,7,105]



def posicinar_maximo(lista:list)->int:
    '''Toma los números de una lista aleatoria y devuelve
    otra lista con todas las posiciones donde se encontró
    el número más grande

    Args:
        lista(list): Lista con números enteros aleatorios
    
    Returns:
        segunda_lista(list): Lista las posiciones del número máximo
    '''
    flag_maximo = True
    for i in range(len(lista)):
        if flag_maximo == True:
            maximo = lista[i]
            posicion_maximo = i+1
            flag_maximo = False
        else:
            if lista[i] > maximo:
                maximo = lista[i]
                '''
                Si encuentra un nuevo máximo crea una nueva lista vacía
                con espacio para el resto de elementos
                menos los que ya iteró
                '''
                lista_posiciones = [0] * (len(lista) - i)
                for j in range(len(lista_posiciones)):
                    if lista_posiciones[j] == 0:
                        lista_posiciones[j] = i+1
                        break
            else:
                if maximo == lista[i]:
                    for j in range(len(lista_posiciones)):
                        if lista_posiciones[j] == 0:
                            lista_posiciones[j] = i+1
                            break
    



print(f"La/las posicion/es de el valor máximo es/son: {posicinar_maximo(lista)}")