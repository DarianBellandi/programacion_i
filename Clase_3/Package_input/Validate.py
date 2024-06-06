from os import system

def validate_number(numero:int|float,mensaje_error:str,
            minimo:int,maximo:int,intentos:int)->int|float|None:
    match numero:
        case int():
            for i in range(intentos):#Nota: NO toma el valor del último intento
                if numero < minimo or numero > maximo:
                    system("clear")
                    numero = int(input(mensaje_error))
                    valor_retorno = None
                else:
                    valor_retorno = numero
                    break
        case float():
            for i in range(intentos):#Nota: NO toma el valor del último intento
                if numero < minimo or numero > maximo:
                    system("clear")
                    numero = float(input(mensaje_error))
                    valor_retorno = None
                else:
                    valor_retorno = numero
                    break
    return valor_retorno

def validate_length(texto:str,mensaje_error:str,
               longitud:int,intentos:int)->str|None:
    for i in range(intentos):#Nota: NO toma el valor del último intento
        if len(texto) != longitud:
            system("clear")
            texto = input(mensaje_error)
            valor_retorno = None
        else:
            valor_retorno = texto
            break
    return valor_retorno