from package_strings.strings_functions import *
'''
Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.
'''
cadena = "neuquen"

def es_palindromo(cadena):
    valor_retorno = True
    if slicing_string(cadena,0,len(cadena)) != slicing_string(cadena,0,len(cadena),-1):
        valor_retorno = False
    return valor_retorno

print(es_palindromo(cadena))

