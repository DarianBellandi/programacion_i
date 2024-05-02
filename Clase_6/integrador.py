from os import system
from Package_Arrays.Array_Generales import *
from Package_Arrays.Especificas import *
from Package_Input.Input import *

'''
Menú - Arrays -  Funciones

Realizar un menú de opciones en donde el usuario pueda realizar las siguientes 
operaciones:
Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
Mostrar la cantidad de números positivos y negativos.
Mostrar la sumatoria de los números pares.
Informar el mayor de los números impares.
Listar todos los números ingresados.
Listar todos los números pares.
Listar los números de las posiciones impares.  
Salir


Notas:

Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya
ingresado los datos solicitados.

Todas las opciones deberán ser programadas en funciones: habrá funciones 
específicas (por ejemplo para determinar si un número es positivo o negativo) y 
funciones de nivel general (por ejemplo una función que liste los números pares).

Tener en cuenta las características de la programación funcional.

Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras 
que las generales en el módulo “Array_Generales.py”. Todos estos módulos deben 
estar integrados en el paquete Package_Arrays.

Utilizar las funciones input del paquete Package_Input.


Consejo: Primero realizar el desarrollo de las funciones y probarlas. Luego, armar 
los módulos y paquetes.

'''
    
def pausar():
    input("Presiona Enter para continuar...") 

system("clear")

una_lista = [0] * 10

bandera_ingreso = False
bandera_seguir = True
while bandera_seguir == True:
    opcion = input("1.Ingresar numeros\n2.Mostrar la cantidad de números positivos y negativos.\n3.Mostrar la sumatoria de los números pares.\n4.Informar el mayor de los números impares.\n5.Listar todos los números ingresados.\n6.Listar todos los números pares.\n7.Listar los números de las posiciones impares.\n8.Salir\nElija una opcion: ")

    match opcion:
        case "1":
            
            for i in range(len(una_lista)):
                una_lista[i] = get_int("Introduce un número entero: ","Error Re-Ingrese numero entero: ",-1000,1000,4)
            system("clear")
            print("Ingresando numeros...")
            bandera_ingreso = True
        case "2":
            if bandera_ingreso == True:
                mostrar_cantidad_positivos_negativos(una_lista)
            else:
                print("No se han ingresado números")

        case "3":
            if bandera_ingreso == True:
                mostar_suma_pares(una_lista)
            else:
                print("No se han ingresado números")
        case "4":
            if bandera_ingreso == True:
                print(f"El mayor de los números impares es el número: {informar_mayor_impares(una_lista)}")
            else:
                print("No se han ingresado números")
        case "5":
            if bandera_ingreso == True:
                print("Todos los números ingresados son:\n")
                listar_numeros(una_lista)
            else:
                print("No se han ingresado números")
        case "6":
            if bandera_ingreso == True:
                print("Todos los números pares son:\n")
                listando_numeros_pares(una_lista)
            else:
                print("No se han ingresado números")
        case "7":
            if bandera_ingreso == True:
                print("Números de las posiciones impares:\n")
                listando_numero_pos_impar(una_lista)
            else:
                print("No se han ingresado números")
        case "8":
            bandera_seguir = False
    pausar()
    system("clear")
