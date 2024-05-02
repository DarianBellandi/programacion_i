'''
Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
'''
#Nombre completo: Darian Bellandi

def solitando_numero_entero(minimo:int,maximo:int) -> int:
    numero = int(input("Ingrese numero entero: "))
    while numero > maximo or numero < minimo:
        numero = int(input("ERROR - Re-Ingrese numero entero: "))

    return numero

def solicitando_numero_flotante(minimo:int,maximo:int)-> float:
    numero = float(input("Ingrese numero flotante: "))
    while numero > maximo or numero < minimo:
        numero = float(input("ERROR - Re-Ingrese numero flotante: "))
    return numero

def solicitando_string(longitud:int)->str:
    cadena_texto = input("Ingrese texto: ")
    while len(cadena_texto) != longitud:
        cadena_texto = input("Re-Ingrese texto: ")
    return cadena_texto
