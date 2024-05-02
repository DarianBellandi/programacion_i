'''
Realizar una función recursiva que la suma de los dígitos de un número.
'''
#Nombre completo: Darian Bellandi

def sumar_digitos(numero:int)->int:
    if numero > 9:
        valor_retorno = numero % 10 + sumar_digitos(numero // 10)
    else:
        valor_retorno = numero
    return valor_retorno

print(sumar_digitos(6274))