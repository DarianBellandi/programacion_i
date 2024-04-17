'''
UTN TECHNOLOGIES

UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

'''
#Nombre completo: Darian Bellandi
#Division: 211-1
#DNI: 43796835

contador_ia = 0
contador_ia_iot_masculino_25_50 = 0
contador_iot = 0
contador_rv_ra = 0
contador_no_fem_no_ia_30_40 = 0
flag_masculino_mayor = False
for empleado in range(10):
    #Ingreso de datos del empleado
    print(f"Datos empleado n°{empleado+1}")
    nombre = input("Ingrese nombre: ")
    
    edad = int(input("Ingrese edad: "))
    while edad < 18:
        edad = int(input("Reingrese edad: "))

    genero = input("Ingrese género: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Reingrese género: ")

    tecnologia_votada = input("Ingrese tecnología votada: ")
    while tecnologia_votada != "IA" and tecnologia_votada != "RV/RA" and tecnologia_votada != "IOT":
        tecnologia_votada = input("Reingrese tecnología votada: ")
    
    #Procesamiento de datos en base a la tecnología votada
    match tecnologia_votada:
        case "IA":
            contador_ia = contador_ia + 1
            if genero == "Masculino":
                if flag_masculino_mayor == False:
                    edad_masculino_mayor = edad
                    nombre_masculino_mayor = nombre
                    tec_votada_masculino_mayor = tecnologia_votada
                    flag_masculino_mayor = True
                else:
                    if edad_masculino_mayor < edad:
                        edad_masculino_mayor = edad
                        nombre_masculino_mayor = nombre
                        tec_votada_masculino_mayor = tecnologia_votada

                if edad >= 25 and edad <= 50:
                    contador_ia_iot_masculino_25_50 = contador_ia_iot_masculino_25_50 + 1

        case "IOT":
            contador_iot = contador_iot + 1
            if genero == "Masculino":
                if flag_masculino_mayor == False:
                    edad_masculino_mayor = edad
                    nombre_masculino_mayor = nombre
                    tec_votada_masculino_mayor = tecnologia_votada
                    flag_masculino_mayor = True
                else:
                    if edad_masculino_mayor < edad:
                        edad_masculino_mayor = edad
                        nombre_masculino_mayor = nombre
                        tec_votada_masculino_mayor = tecnologia_votada

                if edad >= 25 and edad <= 50:
                    contador_ia_iot_masculino_25_50 = contador_ia_iot_masculino_25_50 + 1
                    if edad >= 33 and edad < 40:
                        contador_no_fem_no_ia_30_40 = contador_no_fem_no_ia_30_40 + 1

            else:
                if genero == "Otro" and edad >= 33 and edad <= 40:
                    contador_no_fem_no_ia_30_40 = contador_no_fem_no_ia_30_40 + 1

        case _: #utilizo default ya que previamente se verificó el ingreso de datos
            contador_rv_ra = contador_rv_ra + 1
            if genero == "Otros":
                if edad >= 33 and edad <= 40:
                    contador_no_fem_no_ia_30_40 = contador_no_fem_no_ia_30_40 + 1
            else:
                if genero == "Masculino":
                    if flag_masculino_mayor == False:
                        edad_masculino_mayor = edad
                        nombre_masculino_mayor = nombre
                        tec_votada_masculino_mayor = tecnologia_votada
                        flag_masculino_mayor = True
                    else:
                        if edad_masculino_mayor < edad:
                            edad_masculino_mayor = edad
                            nombre_masculino_mayor = nombre
                            tec_votada_masculino_mayor = tecnologia_votada

                    if edad >= 33 and edad <= 40:
                        contador_no_fem_no_ia_30_40 = contador_no_fem_no_ia_30_40 + 1
print("\n\n")
porcentaje_total = contador_ia + contador_iot + contador_rv_ra
porcentaje_no_fem_no_ia_30_40 = contador_no_fem_no_ia_30_40 * 100 / porcentaje_total

mensaje = f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive: {contador_ia_iot_masculino_25_50}\n\nPorcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje_no_fem_no_ia_30_40}%\n\nNombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género:\n\tNombre: {nombre_masculino_mayor}\n\tTecnología: {tec_votada_masculino_mayor}\n"

print(mensaje)