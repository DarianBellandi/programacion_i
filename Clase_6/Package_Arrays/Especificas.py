def informar_mayor_impares(lista:list)->int:
    '''Toma los números ingresados por lista y el número más grande
        de los impares
    Args:
        lista(list): Lista de números enteros

    Return
        maximo(int): El numero más grande de los impares
    '''
    flag_maximo = True
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            if flag_maximo == True:
                maximo = lista[i]
                flag_maximo = False
            else:
                if maximo < lista[i]:
                    maximo = lista[i]
    return maximo




def mostar_suma_pares(lista:list)->None:
    '''Toma los números ingresados por lista y el número más grande
        de los impares
    Args:
        lista(list): Lista de números enteros

    Return
        maximo(int): El numero más grande de los impares
    '''
    suma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            suma += lista[i]
        
    print(f"La suma de todos los números pares es: {suma}")
    return None





def mostrar_cantidad_positivos_negativos(lista:list)->None:
    '''Toma los números ingresados por lista y muestra la cantidad de positivos y negativos
    Args:
        lista(list): Lista de números enteros

    Returns:
        None
    '''
    contador_positivo = 0
    contador_negativo = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            contador_positivo += 1
        else:
            contador_negativo +=1
    mensaje = f"La cantidad de posisivos son {contador_positivo}\nLa cantidad de negativos son {contador_negativo}"
    print(mensaje)
    return None