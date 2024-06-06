from os import system
from sys import path

path.append("Clase_3/Package_input")
from Input import *

system("clear")

filas_a = get_int("Ingnrese filas de la matriz A: ","Error reingrese filas",1,100,4)
columnas_a = get_int("Ingrese columnas de la matriz A: ","Error reingrese columnas",1,100,4)

print(" ")

filas_b = get_int("Ingrese filas de la matriz B: ","Error reingrese filas",1,100,4)
columnas_b = get_int("Ingrese columnas de la matriz B: ","Error reingrese columnas",1,100,4)

print(" ")

if columnas_a == filas_b:
    matriz_a = [[0] * columnas_a for _ in range(filas_a)]
    matriz_b = [[0] * columnas_b for _ in range(filas_b)]

    matriz_producto = [[0] * columnas_b for _ in range(filas_a)]

    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[i])):
            matriz_a[i][j] = get_int(f"Valor matriz A {i+1}x{j+1}: ",f"Error reingrese valor matriz A {i+1}x{j+1}: ",-100,100,4)
    print(" ")
    for i in range(len(matriz_b)):
        for j in range(len(matriz_b[i])):
            matriz_b[i][j] = get_int(f"Valor matriz B {i+1}x{j+1}: ",f"Error reingrese valor matriz B {i+1}x{j+1}: ",-100,100,4)
    print("\nResultado: \n")
    for i in range(len(matriz_producto)):
        for j in range(len(matriz_producto[i])):
            for k in range(len(matriz_b)):# nota: k itera para calcular la suma de los productos entre las filas de A y columnas de B
                matriz_producto[i][j] += matriz_a[i][k] * matriz_b[k][j]

    #Se muestra el resultado de la matriz producto
    for i in range(len(matriz_producto)):
        for j in range(len(matriz_producto[0])):
            print(matriz_producto[i][j],end=" ")
        print(" ")

else:
    system("clear")
    print(f"Esta multiplicación de matrices no puede realizarce debido a:\n\tOrden matriz A: {filas_a}x{columnas_a}\n\tOrden matriz B: {filas_b}x{columnas_b}")