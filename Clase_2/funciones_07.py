'''
Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
'''
#Nombre completo: Darian Bellandi

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

# numero1 = int(input("Ingrese primer número: "))
# numero2 = int(input("Ingrese segundo número: "))
# numero3 = int(input("Ingrese el tercer número: "))

# numero_mayor = obteniendo_numero_mayor(numero1,numero2,numero3)
# print(f"El numero mayor es: {numero_mayor}")