#Limite de recursividad es 996
#Overflowing
#pilas van variables locales y llamadas

numero = 500
def calcular_factorial(numero:int):
    if numero != 0:
        factorial = numero * calcular_factorial(numero -1)
    else:
        factorial = 1
    return factorial


'''
numero = 0
factorial = 1
i = numero
while i != 0:
    factorial *= i
    i-= 1
'''
print(f"El factorial de {numero} es {calcular_factorial(numero)}")
#print(f"El factorial de {numero} es {factorial}")