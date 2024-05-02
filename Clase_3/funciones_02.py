'''
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido.

Nota: utilizar la función len.
'''
#Nombre completo: Darian Bellandi

def get_string(mesanje:str,mensaje_error:str,
               longitud:int,intentos:int)->str|None: 
    texto = input(mesanje)
    for i in range(intentos):#Nota: NO toma el valor del último intento
        if len(texto) != longitud:
            texto = input(mensaje_error)
            valor_retorno = None
        else:
            valor_retorno = texto
            break
    return valor_retorno