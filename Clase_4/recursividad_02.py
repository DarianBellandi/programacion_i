'''
Realizar una función recursiva que calcule la potencia de un número:
'''
#Nombre completo: Darian Bellandi

def calculando_potencia(base:float,exponente:int)->float:
    if exponente == 1:
        valor_retorno = base
    else:
        if exponente == 0:
            valor_retorno = 1
        else:
            valor_retorno = base * calculando_potencia(base,exponente-1)
    return valor_retorno

print(calculando_potencia(3,3))