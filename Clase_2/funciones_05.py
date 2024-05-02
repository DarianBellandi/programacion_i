from math import pi
'''
Escribe una función que calcule el área de un círculo. La función
debe recibir el radio como parámetro y devolver el área.
'''
#Nombre completo: Darian Bellandi

def calculando_area_circulo(radio: float)-> float:
    area_circulo = 3.1415 * radio**2
    return area_circulo

# radio_circulo = float(input("Ingrese radio del circulo: "))
# area_circulo = calculando_area_circulo(radio_circulo)
# print(f"El area del circulo es: {area_circulo}")