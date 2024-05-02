from math import pi
def solitando_numero_entero() -> int:
    #Solicita un entero y lo retorna
    numero = int(input("Ingrese numero entero: "))
    return numero

def solicitando_numero_flotante()-> float:
    numero = float(input("Ingrese numero flotante: "))
    return numero

def solicitando_string()->str:
    cadena_texto = input("Ingrese texto: ")
    return cadena_texto

def calculando_area_circulo(radio: float)-> float:
    area_circulo = pi * radio**2
    return area_circulo

def obteniendo_numero_mayor(numero1:int,numero2:int,numero3:int)->int:
    if numero1 > numero2:
        if numero1 > numero3:
            numer_mayor = numero1
        else:
            numer_mayor = numero3
    else:
        if numero2 > numero3:
            numer_mayor = numero2
        else:
            numer_mayor = numero3
    return numer_mayor

def calculando_potencia(base:float,exponente:int)->float:
    return base**exponente
