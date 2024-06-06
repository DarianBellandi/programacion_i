'''
Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
'''

#cadena = "HOlaosE"
#excluidos = "aeiouAEIOU"

def suprimir_vocales(cadena,caracteres_excluidos):
    cadena_2 = ""
    for i in range(len(cadena)):
        flag_vocal = False
        for j in range(len(caracteres_excluidos)):
            if cadena[i] == caracteres_excluidos[j]:
                flag_vocal = True
                break
        if flag_vocal == False:
            cadena_2 += cadena[i]
    return cadena_2
#print(suprimir_vocales(cadena,excluidos))