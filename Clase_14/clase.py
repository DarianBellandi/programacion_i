import re
import json
#ARCHIVOS

#OPERACIONES 
#APERTURA
'''
archivo = open(r"mi_archivo.txt",'w')#devuelve un objeto tipo file

#USO
#archivo.write("Voy a estudiar")
#archivo.closed
#archivo.name
#archivo.mode

#LO CIERRO
archivo.close()

archivo = open(r"mi_archivo.txt",'r')
cadena = archivo.read()
archivo.close
print(cadena)

lista = ['Giovani','Luis','Maria','Pedro']
texto = "" 
for nombre in lista:
    nombre = str(nombre)
    texto += f"{nombre}\n"

with open('lista.txt','w') as archivo:# with es un administrador de contexto
    archivo.write(texto)

with open('lista.txt','r') as archivo:
    lista = archivo.readline()

with open('archivo.txt','r') as archivo:
    for linea in archivo:
        print(linea)

lista = ['Giovani','Luis','Maria','Pedro']
texto = "" 
for nombre in lista:
    nombre = str(nombre)
    texto += f"{nombre}\n"

with open('archivo.txt','r') as archivo:
    archivo.write(texto)


nombres = ['Jose','Maria','Luis']
apellidos = ['Gomez','Lopez','Ruiz']
edads = [45,24,19]

#for i 

with open('agenda.csv','w') as agenda:
    for i in range(len(nombres)):
        linea = f'{},{},{}'


with open('agenda.csv','w') as agenda:
    for linea in agenda:
        registro = re.split(',|\n',linea)
        print(f"{registro[0]} -- {registro[1]} -- {registro[2]}")
'''
lista = [
    {'nombre': 'juan','edad': 25},
    {'nombre': 'maria','edad': 14},
    {'nombre': 'luis','edad': 25}
    ]

with open('personas.json','w') as archivo:
    json.dump(lista,archivo, indent=4)

with open('personas.json','r') as archivo:
    data = json.load(archivo)

for persona in data:
    print(f'{persona['nombre']}')