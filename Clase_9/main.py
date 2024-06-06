cadena = "HOLA C3MO ESTAN?"

for i in range(len(cadena)):
    caracter_minuscula = cadena[i]
    if cadena[i] >= "A" and cadena[i] <= "Z":
        orden = ord(cadena[i]) + 32
        caracter_minuscula = chr(orden)
    cadena_2 = caracter_minuscula

