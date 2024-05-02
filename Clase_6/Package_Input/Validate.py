def is_int(cadena_texto):
    if cadena_texto == "":
        valor_retorno = False
    else:
        if cadena_texto[0] == "-":
            if cadena_texto == "-":
                valor_retorno = False
            else:
                cadena_texto = cadena_texto[1:]
        for caracter in cadena_texto:
            if (caracter < '0' or caracter > '9'):
                valor_retorno = False
                break
            else:
                valor_retorno = True
    return valor_retorno

def is_float(cadena_texto):
    if cadena_texto == "":
        valor_retorno = False
    else:
        if cadena_texto[0] == '-':
            if cadena_texto == '-':
                valor_retorno = False
            cadena_texto = cadena_texto[1:]

        punto_encontrado = False
        for caracter in cadena_texto:
            if caracter == '.':
                if punto_encontrado:
                    valor_retorno = False
                punto_encontrado = True
            else:
                if caracter < '0' or caracter > '9':
                    valor_retorno = False
                else:
                    valor_retorno = True

    return valor_retorno


def validate_number(numero:int|float,mensaje_error:str,
            minimo:int,maximo:int,intentos:int)->int|float|None:
    match numero:
        case int():
            for i in range(intentos):#Nota: NO toma el valor del último intento
                if numero < minimo or numero > maximo:
                    numero = int(input(mensaje_error))
                    valor_retorno = None
                else:
                    valor_retorno = numero
                    break
        case float():
            for i in range(intentos):#Nota: NO toma el valor del último intento
                if numero < minimo or numero > maximo:
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
            texto = input(mensaje_error)
            valor_retorno = None
        else:
            valor_retorno = texto
            break
    return valor_retorno