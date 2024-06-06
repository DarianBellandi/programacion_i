#C
def crear_alumano(dni:int,nombre:str,apelldio:str,nota:int)-> dict:
    dicionario_alumano = {
                        'dni': dni,
                        'nombre': nombre,
                        'apellido': apelldio,
                        'nota': nota
                        }
    
    return dicionario_alumano

def ingresar_alumano_lista(lista_alumno:list):
    dni = input('ingrese dni')
    nombre = input('ingrese nombre')
    apellido = input('ingrese apellido')
    nota = input('ingrese nota')

    diccionario = crear_alumano(dni,nombre,apellido,nota)
    lista_alumno.append(diccionario)


#R
def mostrar_alumno(alumno):
    print(f"DNI: {alumno['dni']:10} |\tNombre {alumno['nombre']:>12} |\tApellido: {alumno['apellido']} |\tNota: {alumno['nota']}")

def mostrar_lista_alumano(lista_alumnos):
    for alumno in lista_alumnos:
        mostrar_alumno(alumno)

#U
def modificar_alumno(lista_alumnos,dni):
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]['dni'] == dni:
            valor_i = i
            break
    que_modifica = input("Que desea modificar")
    match que_modifica:
        case 'nombre':
            nombre = input('que nombre')
            lista_alumnos[valor_i]['nombre'] = nombre
        case 'apellido':
            apellido = input('que apellido')
            lista_alumnos[valor_i]['apellido'] = apellido
        case 'nota':
            nota = input('que nota')
            lista_alumnos[valor_i]['nota'] = nombre

    
    


#D
def eliminar_alumno(lista_alumnos:list,dni: int):
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]['dni'] == dni:
            valor_i = i
            break
    
    lista_eliminados = lista_alumnos.pop(valor_i)
    return lista_eliminados