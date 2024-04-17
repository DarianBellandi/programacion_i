'''
Crea una función que verifique si un número dado es par o impar. La función
debe imprimir un mensaje indicando si el número es par o impar.
'''
#Nombre completo: Darian Bellandi

x = int(input("Ingrese numero: "))

def mi_funcion(x):
    
    if x % 2 == 0:
        mensaje = "es par"
    else:
        mensaje = "es impar"
    return mensaje

mensaje = mi_funcion(x)
print(mensaje)