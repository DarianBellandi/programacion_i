from Data import *
#from os import path
#path.exists
'''
def generar_csv(path: str,lista: list):
    archivo = open(path,'w',encoding='utf8')
    linea = ''
    for tema in lista:
        linea += f"{tema['title']},{tema['views']},{tema['length']}\n"
    archivo.write(linea)
    archivo.close

generar_csv('playlist.csv',lista_bzrp)
        
'''

def parser_csv(path:str)-> list:
    lista = []

try:
    archivo = open('archivo.txt','r')
    cadena = archivo.read()
    print(cadena)
except:
    print('archivo no existente')