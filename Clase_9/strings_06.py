from package_strings.strings_functions import slicing_string
'''
Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
'''
#cadena = "El pan del panadero"
#sub_cadena = ""

def contar_repeticiones(cadena,sub_cadena):
    acumulador = 0
    for i in range(len(cadena)-len(sub_cadena)):
        if slicing_string(cadena,i,len(sub_cadena)+i,1) == sub_cadena:
            acumulador += 1
    print(acumulador)

#contar_repeticiones(cadena,sub_cadena)