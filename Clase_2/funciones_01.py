'''
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
'''
#Nombre completo: Darian Bellandi

def solitando_numero_entero() -> int:
    #Solicita un entero y lo retorna
    numero = int(input("Ingrese numero entero: "))
    return numero

numero_entero = solitando_numero_entero()
print(numero_entero)