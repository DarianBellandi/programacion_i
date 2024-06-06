'''
CASO INVESTIGACIÓN CRIMINAL: CSI UTN 

Se ha encontrado una muestra de ADN en el lugar del crimen que contiene la
siguiente secuencia de bases nitrogenadas: “CGTTTAATG”. La investigación ha
revelado tres posibles sospechosos, cada uno con su propia muestra de ADN:

Juan Pérez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
María Rodríguez
Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
Carlos Sánchez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

Para resolver el caso, nos piden que desarrollemos un programa que compare las
combinaciones de bases nitrogenadas de la muestra encontrada con las muestras
de los sospechosos. 
Mostrar el nombre por pantalla en caso de encontrar al asesino, o la leyenda
“SON TODOS INOCENTES”. 
'''
#Nombre completo: Darian Bellandi

def comparar_muestra_culpable(muestra_sospechoso:str,muestra_recolectada:str)-> bool:
    '''Realiza una comparacion de la muestra de ADN encrada en la escena del 
    crimen con la muestra proporcionada de los sospechosos, en caso de ser
    compatible devuelve 'True'

    Args:
        muestra_sospechoso (str): muestra ADN extraida de los sospechosos

        muestra_recolectada (str): muestra ADN de la escena del crimen

    Returns:
        culpable (bool): True | False


    '''
    culpable = False
    for i in range(len(muestra_sospechoso) + 1 - len(muestra_recolectada)):
        if muestra_sospechoso[i:len(muestra_recolectada)+i] == muestra_recolectada:
            culpable = True
            break
    
    return culpable


muestra_adn_juan_perez = "CGGGGCTAAAATTTTTTACGATCG"
muestra_adn_maria_rodriguez = "AACGTTTAATGTTCTAAGCTGCG"
muestra_adn_carlos_sanchez = "CGGGGCTAAAATTTTTTACGATCG"

muestra_recolectada = "CGTTTAATG"

mensaje = "SON TODOS INOCENTES"
if comparar_muestra_culpable(muestra_adn_juan_perez,muestra_recolectada):
    mensaje = 'EL CULPABLE ES JUAN PEREZ'
else:
    if comparar_muestra_culpable(muestra_adn_maria_rodriguez,muestra_recolectada):
        mensaje = 'EL CULPABLE ES MARIA RODRIGUEZ'
    else:
        if comparar_muestra_culpable(muestra_adn_carlos_sanchez,muestra_recolectada):
            mensaje = 'EL CULPABLE ES CARLOS SÁNCHEZ'


print(mensaje)



