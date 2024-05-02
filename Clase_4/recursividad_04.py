from Input import *
'''
Realizar una función para calcular el número de Fibonacci de un número ingresado
por consola.

Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente
es la suma de los dos anteriores:

En donde:
número: el número ingresado por el usuario mediante consola, utilizando nuestra
función get_int(mensaje,mensaje_error,mínimo,máximo,reintentos)
'''
#Nombre completo: Darian Bellandi


'''
def get_int(mesanje:str,mensaje_error:str,
            minimo:int,maximo:int,intentos:int)->int|None:
    numero = int(input(mesanje))
    
    for i in range(intentos):#Nota: NO toma el valor del último intento
                if numero < minimo or numero > maximo:
                    numero = int(input(mensaje_error))
                    valor_retorno = None
                else:
                    valor_retorno = numero
                    break
    return valor_retorno
'''
    
def fibonacci(numero:int)->int:
    if numero <= 0:
        valor_retorno = 0
    else:
        if numero == 1:
            valor_retorno = 1
        else:
            valor_retorno = fibonacci(numero-1) + fibonacci(numero-2)
    return valor_retorno

print(fibonacci(get_int("Ingrese un numero: ","Error Re-Ingrese un numero",0,20,6)))