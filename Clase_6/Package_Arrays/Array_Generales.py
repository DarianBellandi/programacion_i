def listar_numeros(lista:int)->None:
    '''Toma los números ingresados por lista y los muestra por pantalla
    Args:
        lista(list): Lista de números enteros

    Return
        None
    '''
    for i in range(len(lista)):
        print(f"{i+1} -> {lista[i]}")

    return None

def listando_numeros_pares(lista:int):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(f"{i+1} -> {lista[i]}")
    return None

def listando_numero_pos_impar(lista:list):
    for i in range(len(lista)):
        if i % 2 == 0:
            print(f"{i+1} -> {lista[i]}")
    return None