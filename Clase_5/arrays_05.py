'''
Escribir una función que reciba como parámetros una list de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
'''
#Nombre completo: Darian Bellandi


def mostrar_posicion_maximo(list:list)->int:
    '''Toma los números de una lista aleatoria y muestra
    por pantalla todas las posiciones donde se encontró
    el número más grande

    Args:
        lista(list): Lista con números enteros aleatorios
    
    Returns:
            None
    '''
    flag_maximo = True
    lista_posiciones = [0] * len(list)
    for i in range(len(list)):
        if flag_maximo == True:
            maximo = list[i]
            lista_posiciones[0] = i+1
            flag_maximo = False
        else:
            if list[i] > maximo:
                maximo = list[i]
                '''
                Si encuentra un nuevo máximo crea una nueva lista vacía
                con espacio para el resto de elementos
                menos los que ya iteró
                '''
                lista_posiciones = [0] * (len(list) - i)
                for j in range(len(lista_posiciones)):
                    if lista_posiciones[j] == 0:
                        lista_posiciones[j] = i+1
                        break
            else:
                if maximo == list[i]:
                    for j in range(len(lista_posiciones)):
                        if lista_posiciones[j] == 0:
                            lista_posiciones[j] = i+1
                            break
    

    
    #Limpieza de elemtos con ceros
    contador = 0
    for elemento in lista_posiciones:
        if elemento != 0:
            contador += 1

    lista_posiciones_sin_ceros = [0] * contador
    indice = 0
    
    for elemento in lista_posiciones:
        if elemento != 0:
            lista_posiciones_sin_ceros[indice] = elemento
            indice += 1



    #Salida de datos por pantalla
    print(f"El número máximo ({maximo}) se encontró:\n")
    for i in lista_posiciones_sin_ceros:
        print(f"\tEn la posición {i}")

    return None



#lista = [34,34,8,15,34,4,6,34,31,32,33,2,34,2]
#mostrar_posicion_maximo(lista)