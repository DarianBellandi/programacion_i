def consultar_existencia_legajo(chofer_legajo:int,matriz_legajos:list)->bool | int:
    '''Consulta la existencia del legajo ingresado en una la matriz
    Args:
        chofer_legajo(int): Legajo a validar

        matriz_legajos(list): Matriz de legajos

    Returns:
        valor_retorno(bool): True | False
    '''
    for i in range(len(matriz_legajos)):
        for j in range(len(matriz_legajos)):
            if chofer_legajo == matriz_legajos[i][j]:
                valor_retorno = True
                break
            else:
                valor_retorno = False
        if valor_retorno == True:
            break
    return valor_retorno

def mostrar_recaudacion(matriz_linea):
    for j in range(len(matriz_linea[0])):
        for i in range(len(matriz_linea)):
            print(f"Recaudación línea {j+1} coche {i+1}: {matriz_linea[i][j]}")


def mostrar_recaudacion_linea(matriz_linea):
    for j in range(len(matriz_linea[0])):
        acumulador_coches = 0
        for i in range(len(matriz_linea)):
            acumulador_coches += matriz_linea[i][j]
        print(f"RECAUDACIÓN LÍNEA {j+1}: {acumulador_coches}")

def mostrar_recaudacion_coche(matriz_linea):
    for i in range(len(matriz_linea)):
        acumulador_coches = 0
        for j in range(len(matriz_linea[i])):
            acumulador_coches += matriz_linea[i][j]
        print(f"Recaudación coche {i+1}: {acumulador_coches}")

def calcular_recaudacion_total(matriz_linea):
    acumulador_coches = 0
    for i in range(len(matriz_linea)):
        for j in range(len(matriz_linea[i])):
            acumulador_coches += matriz_linea[i][j]
    print(f"Acumulación total: {acumulador_coches}")
    
        