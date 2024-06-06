import time
#c = 0  # Inicializar el contador de 

def quick_sort_iterativo(array):
    #global c
    # Pila para mantener los índices de sub-arreglos, con un tamaño inicial grande
    stack = [0] * (len(array) * 2)
    stack_size = 0  # Tamaño inicial de la pila

    # Inicializar la pila con el rango inicial
    stack[stack_size] = 0
    stack_size += 1
    stack[stack_size] = len(array) - 1
    stack_size += 1

    while stack_size > 0:
        # Extraer low y high de la pila
        stack_size -= 1
        high = stack[stack_size]
        stack_size -= 1
        low = stack[stack_size]

        if low < high:
            pi = particionar(array, low, high)
            #c += 1  # Incrementar el contador de iteraciones

            # Agregar los índices de los sub-arreglos a la pila
            stack[stack_size] = low
            stack_size += 1
            stack[stack_size] = pi - 1
            stack_size += 1

            stack[stack_size] = pi + 1
            stack_size += 1
            stack[stack_size] = high
            stack_size += 1
            
    return array

def particionar(array, low, high):
    pivote = array[high]  # El pivote será el último elemento del sub-arreglo
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]  # Colocar el pivote en su posición correcta

    return i + 1

'''
#Ejemplo de uso
#vector = [5, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7]

start = time.time()
quick_sort_iterativo(vector)
end = time.time()
print(f"Tiempo: {(end - start)*1000}")
print(f"cantidad iteraciones: {c}")
print(len(vector))
'''