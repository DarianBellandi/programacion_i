'''
Desarrollar una función que reciba como parametros el precio de un producto, la cantidad y el porcentaje de descuento que se aplicara si la cantidad de productos supera las 10 unidades. La funcion retornara el precio de la compra con descuento (si corresponde).  (Enviar aqui link de GDB)
'''

def calando_precio_cantidad_10(precio:float,cantidad:int,
                               porcenjate_descuento:int)->float:
    if cantidad > 10:
        if porcenjate_descuento > 0:
            valor_retorno = (precio * cantidad) -(precio * cantidad * porcenjate_descuento // 100)
        else:
            valor_retorno = precio * cantidad
    else:
        valor_retorno = None
    return valor_retorno


