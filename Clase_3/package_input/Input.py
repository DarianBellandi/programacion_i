from Validate import *
''''
Realizar un paquete denominado Package_Input, el mismo deberá contener los siguientes módulos:
Input.py
    get_int()
    get_float()
    get_string()
Validate.py
    validate_number()
    validate_length()

Nota: estas funciones las tendrán que desarrollar en el módulo Validate y utilizar en el módulo Input.py para realizar las validaciones necesarias.

'''

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

#print(get_float("Ingrese un número","Re-Ingrese un número",4,8,3))

'''
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido
'''

def get_string(mesanje:str,mensaje_error:str,
               longitud:int,intentos:int)->str|None: 
    texto = input(mesanje)
    valor_retorno = validate_length(texto,mensaje_error,longitud,intentos)

    return valor_retorno

#print(get_string("Escriba aquí","Error escriba nuevamente",4,3))