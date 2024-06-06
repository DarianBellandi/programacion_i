from os import system
from sys import path
path.append("Clase_3/Package_input")
from Input import *
from random import randint
from Clase_7.modulos_planilla_practica_matrices_obsoleto import *
'''
Práctica de Matrices
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene
15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:
Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro
de una matriz de legajos). Si el chofer existe cargará la recaudación del
viaje indicando línea y coche (no necesariamente un chofer está asignado a una
única línea y coche), estos datos deben estar validados. Un chofer puede 
cargar más de una recaudación por día (para distintas líneas y distintos
coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
Mostrar la recaudación de cada coche y línea.
Calcular y mostrar recaudación por línea.
Calcular y mostrar recaudación por coche.
Calcular y mostrar la recaudación total.
Salir
Todo el desarrollo tiene que estar modularizado: ingreso de datos,
validaciones de líneas y coches, generación y verificación de existencia de
legajo, cálculos, etc.
'''

system("clear")



lista_legajos = [0] * 15
for i in range(15):
        lista_legajos[i] = randint(1000,9999)

linea_8 = [[0] * 15 for _ in range(5)]
linea_74 = [[0] * 15 for _ in range(5)]
linea_100 = [[0] * 15 for _ in range(5)]


bandera_datos_cargados = False
bandera_seguir = True
while bandera_seguir:
    opcion = input("\t\tMENÚ PLANILLA\n\n1.Cargar planilla\n2.Mostrar la recaudación de cada coche y línea\n3.Calcular y mostrar recaudación por línea\n4.Calcular y mostrar recaudación por coche\n5.Calcular y mostrar la recaudación total.\n6.Salir\nEliga la opción: ")


    match opcion:
        case "1":
            
            print(f"Legajos posibles {lista_legajos}")
            chofer_legajo = int(input("Ingrese su legajo: "))
            legajo_valido, chofer = consultar_existencia_legajo(chofer_legajo,lista_legajos)
            if legajo_valido:
                linea = get_int("Ingrese n° de linea (8 - 74 - 100): ","Error",8,101,5)
                coche = get_int("Ingrese n° de coche (1-5): ","Error",1,6,5)
                coche = coche - 1

                match linea:
                    case 8:
                        linea_8[coche][chofer] = get_int("Ingrese su recaudación: ","Reingrese su recaudación",-100000,100000,5)
                    case 74:
                        linea_74[coche][chofer] = get_int("Ingrese su recaudación: ","Reingrese su recaudación",-100000,100000,5)
                    case 100:
                        linea_100[coche][chofer] = get_int("Ingrese su recaudación: ","Reingrese su recaudación",-100000,100000,5)
                bandera_datos_cargados = True
                print(" ")

            else:
                print("Legajo inválido")



        case "2":
            system("clear")
            if bandera_datos_cargados == True:
                mostrar_recaudacion(linea_8,linea_74,linea_100)
            else:
                print("No se ha ingresado recaudación")

        case "3":
            system("clear")
            if bandera_datos_cargados == True:
                print(calcular_recaudacion_linea(linea_8,linea_74,linea_100))
            else:
                print("No se ha ingresado recaudación")
        
        case "4":
            system("clear")
            if bandera_datos_cargados == True:
                print(calcular_recaudacion_coches(linea_8,linea_74,linea_100))
            else:
                print("No se ha ingresado recaudación")
         
        case "5":
            system("clear")
            if bandera_datos_cargados == True:
                print(calcular_recaudacion_total(linea_8,linea_74,linea_100))
            else:
                print("No se ha ingresado recaudación")
         
        case "6":
            bandera_seguir = False
    pause()
    system("clear")
        