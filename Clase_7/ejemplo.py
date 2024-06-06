#Secuencial
#matriz 


# #Transpuesta
# matriz = [[5,4,8,1],
#           [3,8,2,9],
#           [5,8,3,7]]

# for j in range(len(matriz[0])):
#     for i in range(len(matriz)):
#         print(f"{matriz[j][i]:4}",end = " ")
#     print(" ")


#Multiplicacion escalar

# matriz = [[5,4,8,1],
#           [3,8,2,9],
#           [5,8,3,7]]

# escalar = 3

# matriz_producto = [[0] * len(matriz[0]) for _ in range(len(matriz))]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         matrix_producto[i][j] = matriz[i][j] * escalar

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matrix_producto[i][j],end=" ")
#     print(" ")

#Suma de matrices
matriz_a = [[5,4,8,1],
          [3,8,2,9],
          [5,8,3,7]]

matriz_b = [[5,4,8,1],
            [3,8,2,9],
            [5,8,3,7]]

matriz_suma = [[0] * len(matriz_a[0]) for _ in range(len(matriz_a)) ]
for n in range(len(matriz_a)):
    for m in range(len(matriz_a[n])):
        matriz_suma[n][m] = matriz_a[n][m] + matriz_b[n][m]

matriz_producto = [[0] * len(matriz_a[0]) for _ in range(len(matriz_a))]
escalar = 2
for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
        matriz_producto[i][j] = matriz_a[i][j] * escalar

print("MATRIZ SUMA")
for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
        print(matriz_suma[i][j],end=" ")
    print(" ")
print(" ")


print("MATRIZ PRODUCTO")
for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
        print(matriz_producto[i][j],end=" ")
    print(" ")