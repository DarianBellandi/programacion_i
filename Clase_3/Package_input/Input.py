from Validate import *



def get_int(mensaje:str,mensaje_error:str,
            minimo:int,maximo:int,intentos:int)->int|None:
    
    numero = input(mensaje)
    while is_int(numero) == False:
        numero = input(mensaje_error)
    numero = int(numero)
    valor_retorno = validate_number(numero,mensaje_error,
                                    minimo,maximo,intentos)
    return valor_retorno

def get_float(mensaje:str,mensaje_error:str,
              minimo:int,maximo:int,intentos:int)->float|None:
    numero = input(mensaje)
    while is_float(numero) == False:
        numero = input(mensaje_error)    
    numero = float(numero)
    valor_retorno = validate_number(numero,mensaje_error,
                                    minimo,maximo,intentos)    
    return valor_retorno



def get_string(mesanje:str,mensaje_error:str,
               longitud:int,intentos:int)->str|None: 
    texto = input(mesanje)
    valor_retorno = validate_length(texto,mensaje_error,longitud,intentos)

    return valor_retorno

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

def pause():
    input("Presiona Enter para continuar...") 

