from sys import path
path.append("Clase_3/Package_input")
from Input import *

#INREGRANTES:
#BELLANDI, Darian Adriel
#CAMACHO CISNEROS, Junior Yair
#CONDARCO, Bruno Agustin
#GRACÍA OCAMPO, Delfina
'''
orden = 3  
matriz_cuadrada =  [[8,1,6],
                    [3,5,7],
                    [4,9,2]]
numero_magico = 15
'''

orden = int(input("Ingrese el orden de su matriz: "))

numero_magico = orden * (orden**2+1)/2

matriz_cuadrada = [[0] * orden for _ in range(orden)]



#CARGA DE NUMEROS A LA MATRIZ
for i in range(len(matriz_cuadrada)):
    for j in range(len(matriz_cuadrada[i])):
        matriz_cuadrada[i][j] = get_int("Valor matriz: ","Error",1,orden*orden,5)


#VALIDACIONES

bandera_cuadrado_magico = True

#FIILAS Y COLUMNAS
for i in range(len(matriz_cuadrada)):
    acumulador_fila = 0
    acumulador_comuna = 0
    for j in range(len(matriz_cuadrada[i])):
        acumulador_fila += matriz_cuadrada[i][j]
        acumulador_comuna += matriz_cuadrada[j][i]
    if numero_magico != acumulador_fila or numero_magico != acumulador_comuna:
        bandera_cuadrado_magico = False
        break

#DIAGONAL PRINCIPAL
if bandera_cuadrado_magico == True:
    acumulador_diag_principal = 0
    for i in range(len(matriz_cuadrada)):
        acumulador_diag_principal += matriz_cuadrada[i][i]
    if acumulador_diag_principal != numero_magico:
        bandera_cuadrado_magico = False

#DIAGONAL SECUNDARIA
if bandera_cuadrado_magico == True:
    orden_menos_uno = orden - 1
    acumulador_diag_secundaria = 0
    for i in range(len(matriz_cuadrada)):
        for j in range(len(matriz_cuadrada[i])):
            if i+j == orden_menos_uno:
                acumulador_diag_secundaria += matriz_cuadrada[i][j]
    if acumulador_diag_secundaria != numero_magico:
        bandera_cuadrado_magico = False


if bandera_cuadrado_magico == True:
    print("Es una matriz cuadrado mágico")
else:
    print("No es una matriz cuadro mágico")

