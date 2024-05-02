'''
Escribe una función llamada reemplazar_nombres que reciba como parámetros una
lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La
función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista
con su correspondiente reemplazo y luego retornar la cantidad total de
reemplazos realizados.
'''
#Nombre completo: Darian Bellandi

def reemplazar_nombres(lista:list,nombre:str,reemplazo:str)->str:
    '''Reemplaza los nombres de la lista
    con un nuevo nombre que toma por parámetro

    Args:
        lista(list): Lista con los nombres

        nombre(str): Nombre en la lista a reemplazar
    
        reemplazo(str): Nombre por reemplazar

    Returns:
        mensaje(str): Mensaje con la cantidad de veces que el nombre
        fue reemplazado
    '''
    contador_reemplazos = 0
    for i in range(len(lista)):
        if lista[i] == nombre:
            lista[i] = reemplazo
            contador_reemplazos += 1

    mensaje = f"La cantidad de nombres reemplazados son {contador_reemplazos}"

    return mensaje

'''
lista = ["Juan","Roberto","Martin","Leandro","Pedro","Roberto","Martin",
        "Leandro","Juan","Pedro","Martin"]
print(reemplazar_nombres(lista,"Martin","Mateo"))
print(lista)
'''