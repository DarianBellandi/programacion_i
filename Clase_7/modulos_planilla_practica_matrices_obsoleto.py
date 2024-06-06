def consultar_existencia_legajo(legajo:list,lista_legajos:list)->bool | int:
    for i in range(len(lista_legajos)):
        if legajo == lista_legajos[i]:
            valor_retorno = True
            break
        else:
            valor_retorno = False
    return valor_retorno,i


def mostrar_recaudacion(linea_8,linea_74,linea_100):


    for i in range(len(linea_8)):
        recaudacion_coche = 0
        for j in range(len(linea_8[i])):
            recaudacion_coche += linea_8[i][j]
        print(f"Recadación coche n°{i+1}: {recaudacion_coche}")



    print("\n\tRECAUDACIÓN LINEA 74")
    recaudacion_linea_74 = 0
    for i in range(len(linea_74)):
        recaudacion_coche = 0
        for j in range(len(linea_74[i])):
            recaudacion_coche += linea_74[i][j]
        print(f"Recadación coche n°{i+1}: {recaudacion_coche}")
        
    for i in range(len(linea_100)):
        recaudacion_coche = 0
        for j in range(len(linea_100[i])):
            recaudacion_coche += linea_100[i][j]
        print(f"Recadación coche n°{i+1}: {recaudacion_coche}")
        

    return None

def calcular_recaudacion_linea(linea_8,linea_74,linea_100):


    recaudacion_linea_8 = 0
    for i in range(len(linea_8)):
        recaudacion_coche = 0
        for j in range(len(linea_8[i])):
            recaudacion_coche += linea_8[i][j]
        recaudacion_linea_8 += recaudacion_coche

    recaudacion_linea_74 = 0
    for i in range(len(linea_74)):
        recaudacion_coche = 0
        for j in range(len(linea_74[i])):
            recaudacion_coche += linea_74[i][j]
        recaudacion_linea_74 += recaudacion_coche
    
    recaudacion_linea_100 = 0
    for i in range(len(linea_100)):
        recaudacion_coche = 0
        for j in range(len(linea_100[i])):
            recaudacion_coche += linea_100[i][j]
        recaudacion_linea_100 += recaudacion_coche

    mensaje_recaudacion_lineas = f"RECAUDACION LÍNEA 8: {recaudacion_linea_8}\n\nRECAUDACION LÍNEA 74: {recaudacion_linea_74}\n\nRECAUDACIÓN LINEA 100: {recaudacion_linea_100}\n"

    return mensaje_recaudacion_lineas

def calcular_recaudacion_coches(linea_8,linea_74,linea_100):


    for i in range(len(linea_8)):
        recaudacion_coche = 0
        for j in range(len(linea_8[i])):
            recaudacion_coche += linea_8[i][j]
        match i:
            case 0:
                recaudacion_l8_coche_1 = recaudacion_coche
            case 1:
                recaudacion_l8_coche_2 = recaudacion_coche
            case 2:
                recaudacion_l8_coche_3 = recaudacion_coche
            case 3:
                recaudacion_l8_coche_4 = recaudacion_coche
            case 4:
                recaudacion_l8_coche_5 = recaudacion_coche

    for i in range(len(linea_74)):
        recaudacion_coche = 0
        for j in range(len(linea_74[i])):
            recaudacion_coche += linea_74[i][j]
        match i:
            case 0:
                recaudacion_l74_coche_1 = recaudacion_coche
            case 1:
                recaudacion_l74_coche_2 = recaudacion_coche
            case 2:
                recaudacion_l74_coche_3 = recaudacion_coche
            case 3:
                recaudacion_l74_coche_4 = recaudacion_coche
            case 4:
                recaudacion_l74_coche_5 = recaudacion_coche
    
    for i in range(len(linea_100)):
        recaudacion_coche = 0
        for j in range(len(linea_100[i])):
            recaudacion_coche += linea_100[i][j]
        match i:
            case 0:
                recaudacion_l100_coche_1 = recaudacion_coche
            case 1:
                recaudacion_l100_coche_2 = recaudacion_coche
            case 2:
                recaudacion_l100_coche_3 = recaudacion_coche
            case 3:
                recaudacion_l100_coche_4 = recaudacion_coche
            case 4:
                recaudacion_l100_coche_5 = recaudacion_coche


    mensaje_recaudacion_coches = f"Recaudación coche 1 línea 8: {recaudacion_l8_coche_1}\nRecaudación coche 2 línea 8: {recaudacion_l8_coche_2}\nRecaudación coche 3 línea 8: {recaudacion_l8_coche_3}\nRecaudación coche 4 línea 8: {recaudacion_l8_coche_4}\nRecaudación coche 5 línea 8: {recaudacion_l8_coche_5}\n\nRecaudación coche 1 línea 74: {recaudacion_l74_coche_1}\nRecaudación coche 2 línea 74: {recaudacion_l74_coche_2}\nRecaudación coche 3 línea 74: {recaudacion_l74_coche_3}\nRecaudación coche 4 línea 74: {recaudacion_l74_coche_4}\nRecaudación coche 5 línea 74: {recaudacion_l74_coche_5}\n\nRecaudación coche 1 línea 100: {recaudacion_l100_coche_1}\nRecaudación coche 2 línea 100: {recaudacion_l100_coche_2}\nRecaudación coche 3 línea 100: {recaudacion_l100_coche_3}\nRecaudación coche 4 línea 100: {recaudacion_l100_coche_4}\nRecaudación coche 5 línea 100: {recaudacion_l100_coche_5}\n"

    return mensaje_recaudacion_coches

def calcular_recaudacion_total(linea_8,linea_74,linea_100):
    recaudacion_linea_8 = 0
    for i in range(len(linea_8)):
        recaudacion_coche = 0
        for j in range(len(linea_8[i])):
            recaudacion_coche += linea_8[i][j]

        recaudacion_linea_8 += recaudacion_coche

    recaudacion_linea_74 = 0
    for i in range(len(linea_74)):
        recaudacion_coche = 0
        for j in range(len(linea_74[i])):
            recaudacion_coche += linea_74[i][j]
        recaudacion_linea_74 += recaudacion_coche
    
    recaudacion_linea_100 = 0
    for i in range(len(linea_100)):
        recaudacion_coche = 0
        for j in range(len(linea_100[i])):
            recaudacion_coche += linea_100[i][j]
        recaudacion_linea_100 += recaudacion_coche


    recaudacion_total = recaudacion_linea_8 + recaudacion_linea_74 + recaudacion_linea_100
    mensaje_recuacion_total = f"La recaudación total es {recaudacion_total}"


    return mensaje_recuacion_total