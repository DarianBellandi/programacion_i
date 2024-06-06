'''
Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
'''
cadena = 'wiagcamafvcaexazcx'
caracter = 'f'

def ubicar_caracter(caracter,cadena):
    valor_i = -1
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            valor_i = i+1
            break
    
    return valor_i

print(ubicar_caracter(caracter,cadena))
