from Alumno import *
from os import *
from sys import path
path.append("Clase_3/Package_input")
from Input import *

def pausar():
    input("Presiona Enter para continuar...") 

def mostrar_menu():
    system("clear")
    
    mensaje = "1. Ingresar\n2. Mostrar\n3. Modificar\n4. Eliminar\n5. Salir\nElija una opción: "
    opcion = get_string(mensaje,mensaje,1,4)
    return opcion
        

##############################################################################
lista_estudiantes = [
    {'nombre': 'Juan', 'apellido': 'Pérez', 'dni': 12345678, 'nota': 5},
    {'nombre': 'Ana', 'apellido': 'García', 'dni': 87654321, 'nota': 9},
    {'nombre': 'Luis', 'apellido': 'Martínez', 'dni': 45678912, 'nota': 7},
    {'nombre': 'María', 'apellido': 'Rodríguez', 'dni': 65432198, 'nota': 2},
    {'nombre': 'Carlos', 'apellido': 'Sánchez', 'dni': 23456789, 'nota': 8},
    {'nombre': 'Elena', 'apellido': 'López', 'dni': 98765432, 'nota': 6},
    {'nombre': 'Pablo', 'apellido': 'Gómez', 'dni': 34567891, 'nota': 4},
    {'nombre': 'Sofía', 'apellido': 'Fernández', 'dni': 76543210, 'nota': 6},
    {'nombre': 'Diego', 'apellido': 'Ramírez', 'dni': 56789123, 'nota': 7},
    {'nombre': 'Laura', 'apellido': 'Torres', 'dni': 12398745, 'nota': 9}
]



bandera_datos_cargados = False
while True:
    opcion = mostrar_menu()
    match opcion:
        case '1':
            ingresar_alumano_lista(lista_estudiantes)
            bandera_datos_cargados = True
        case '2':
                mostrar_lista_alumano(lista_estudiantes)
                pausar()
            
        case '3':
            dni = get_int('Ingrese el dni del alumno: ','Dni no válido, reingrese: ',4000000,100000000,4)
            modificar_alumno(lista_estudiantes,dni)
        case '4':
            dni = get_int('Ingrese el dni del alumno: ','Dni no válido, reingrese: ',4000000,100000000,4)
            lista_eliminados = eliminar_alumno(lista_estudiantes,dni)
            print(f"Se ha eliminado al alumno con dni {lista_eliminados['dni']}")
            pausar()
        case '5':
            break
