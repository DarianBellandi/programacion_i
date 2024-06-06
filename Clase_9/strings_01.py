'''
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
'''

cadena = 'murcielaguito'

def contar_vocales(cadena):
    matriz_cantidad_vocales = [[0] * 2 for _ in range(5)]

    matriz_cantidad_vocales[0][0] = "a"
    matriz_cantidad_vocales[1][0] = "e"
    matriz_cantidad_vocales[2][0] = "i"
    matriz_cantidad_vocales[3][0] = "o"
    matriz_cantidad_vocales[4][0] = "u"

    for i in range(len(cadena)):
        match cadena[i]:
            case "a" | "A":
                matriz_cantidad_vocales[0][1] += 1
            case "e" | "E":
                matriz_cantidad_vocales[1][1] += 1
            case "i" | "I":
                matriz_cantidad_vocales[2][1] += 1
            case "o" | "O":
                matriz_cantidad_vocales[3][1] += 1
            case "u" | "U":
                matriz_cantidad_vocales[4][1] += 1
            
    return matriz_cantidad_vocales

'''
matriz_cantidad_vocales = contar_vocales(cadena)
for i in range(len(matriz_cantidad_vocales)):
    for j in range(len(matriz_cantidad_vocales[i])):
        print(matriz_cantidad_vocales[i][j],end=" ")
    print()
'''
