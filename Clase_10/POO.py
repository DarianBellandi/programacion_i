#nombre
#poder
#hablidad
'''
def mostrar_datos(nombre,poder,habilidad,nano):
    print(f"{nombre}{poder}{habilidad}-{nano}")

nombre = "IronMan"
poder = 500
habilidad = "Filantropo millonario"
nanotecnologia = True

mostrar_datos(nombre,poder,habilidad,nanotecnologia)

def mostrar_datos(nombre,poder,habilidad,nano):
    print(f"{nombre}{poder}{habilidad}-{nano}")
mostrar_datos(personaje_1)

'''

from class_personaje import PersonajeJuego

personaje_1 = PersonajeJuego("IronMan",500,"Dispari Utrasónco",True,True)
personaje_2 = PersonajeJuego("Thor",650,"Relampago",True,False)
personaje_3 = PersonajeJuego("BlackWidow",350,"Cuerpo a cuerpo",)
lista_heroes: list[PersonajeJuego] = []
lista_heroes.append(personaje_1)

for heroe in lista_heroes:
    print(heroe.describirse())

for heroe in lista_heroes:
    heroe.volar(1000,200)

#print(personaje_1.describirse())
personaje_1.volar(30,20)

personaje_1.atacar(personaje_2)

'''
TAREA:
*analizar clase list
*

'''



