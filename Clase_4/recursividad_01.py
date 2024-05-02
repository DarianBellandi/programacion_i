'''
Realizar una función recursiva que calcule la suma de los primeros números naturales:
'''
##Nombre completo: Darian Bellandi

def sumando_naturales(numero:int)->int:

    if numero != 1:
        valor_retorno = numero + sumando_naturales(numero-1)
    else:
        valor_retorno = 1
    return valor_retorno

print(sumando_naturales(5))
