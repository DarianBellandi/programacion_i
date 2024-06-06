def slicing_string(cadena,desde,hasta,incremento = 1):
    valor_retorno = ""
    if incremento == -1:
        auxiliar = desde -1
        desde = hasta -1
        hasta = auxiliar
    for i in range(desde,hasta,incremento):
        valor_retorno += cadena[i]
    return valor_retorno