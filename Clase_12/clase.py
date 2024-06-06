#CONCEPTOS
#tupla, desempaquetado, métodos,
#tupla = tuple(lista)
#lista2 = list(tuple)
#tupla.count()
#tupla.index()

#set(es conjuntos),no muestra duplicados,no se ordena(es aleatorio), no es indexable
mi_set = {4,62,6,8,1,5}
#mi_set.add(100)
#mi_set.remove(4) lanza exepcion
#mi_set.discard()

# mi_set2 = {6,61,41,4}

# union = mi_set.union(mi_set2)

# interseccion = mi_set.intersection(mi_set2)

# diferencia_a = mi_set.difference(mi_set2)
# diferencia_b = mi_set2.difference(mi_set)

#DICCIONARIOS, Son mutables, 
mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
}

mi_diccionario["profesion"] = "programador"
print(mi_diccionario.values())
print(mi_diccionario.keys())

for k in mi_diccionario:
    print(f"{k} -> {mi_diccionario[k]}")

for k,v in mi_diccionario.items():
    print(f"{k} -> {v}")