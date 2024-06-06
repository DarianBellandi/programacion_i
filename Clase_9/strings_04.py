'''
Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos
Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
'''

#cadena = "HoolaHH"

def suprimir_char_repetido(cadena):
    cadena_2 = cadena[0]
    for i in range(len(cadena)-1):
        j = i + 1
        if cadena[i] != cadena[j]:
            cadena_2 += cadena[j]
    return cadena_2
        


#print(suprimir_char_repetido(cadena))