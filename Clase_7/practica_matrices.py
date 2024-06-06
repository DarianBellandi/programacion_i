from os import system
from sys import path
path.append("Clase_3/Package_input")
from Input import *
from random import randint
from modulos_planilla import *
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



matriz_legajos = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        matriz_legajos[i][j] = randint(1000,9999)

matriz_lineas = [[0] * 3 for _ in range(5)]


bandera_datos_cargados = False
bandera_seguir = True
while bandera_seguir:
    opcion = input("\t\tMENÚ PLANILLA\n\n1.Cargar planilla\n2.Mostrar la recaudación de cada coche y línea\n3.Calcular y mostrar recaudación por línea\n4.Calcular y mostrar recaudación por coche\n5.Calcular y mostrar la recaudación total.\n6.Salir\nEliga la opción: ")

    match opcion:
        case "1":
            
            print(f"Legajos posibles {matriz_legajos}")
            chofer_legajo = int(input("Ingrese su legajo: "))
            legajo_valido = consultar_existencia_legajo(chofer_legajo,matriz_legajos)
            if legajo_valido:
                linea = get_int("Ingrese línea colectivos: ","Error reingrese línea: ",1,6,4)
                coche = get_int("Ingrese n° coche: ","Error reingrese coche: ",1,6,4)
                linea -= 1
                coche -= 1

                matriz_lineas[coche][linea] = get_int("Ingrese su recaudación: ","Error reingrese su recaudación: ",0,999999,4)                

                bandera_datos_cargados = True
                print(" ")
                continue
            print("Legajo inválido")

        case "2":
            system("clear")
            if bandera_datos_cargados == True:
                mostrar_recaudacion(matriz_lineas)
            else:
                print("No se ha ingresado recaudación")

        case "3":
            system("clear")
            if bandera_datos_cargados == True:
                mostrar_recaudacion_linea(matriz_lineas)
            else:
                print("No se ha ingresado recaudación")
        
        case "4":
            system("clear")
            if bandera_datos_cargados == True:
                mostrar_recaudacion_coche(matriz_lineas)
            else:
                print("No se ha ingresado recaudación")
         
        case "5":
            system("clear")
            if bandera_datos_cargados == True:
                calcular_recaudacion_total(matriz_lineas)
            else:
                print("No se ha ingresado recaudación")
         
        case "6":
            bandera_seguir = False
    pause()
    system("clear")
        