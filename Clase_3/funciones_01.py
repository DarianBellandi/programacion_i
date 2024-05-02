'''
Realizar una función para pedir un número por consola.

En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
Repetir el mismo procedimiento para un dato de tipo float.
'''
#Nombre completo: Darian Bellandi

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

def get_float(mesanje:str,mensaje_error:str,
              minimo:int,maximo:int,intentos:int)->float|None:
    numero = float(input(mesanje))
    for i in range(intentos):#Nota: NO toma el valor del último intento
        if numero < minimo or numero > maximo:
            numero = float(input(mensaje_error))
            valor_retorno = None
        else:
            valor_retorno = numero
            break
    return valor_retorno
