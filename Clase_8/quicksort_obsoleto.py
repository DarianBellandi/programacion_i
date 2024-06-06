import time

def swap(a: int, b: int):
    return b, a

def particionar(array, low, high):
    pivote = array[high]  # El pivote será el último elemento de la lista
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

def quick_sort(array):
    c = 0  # Inicializar el contador de iteraciones

    # Lista como pila para mantener los límites del sub-arreglo
    stack = [(0, len(array) - 1)]
    stack_size = 1

    # Índice para el tope de la pila
    top = 0

    while stack_size > 0:
        low, high = stack[top]
        top -= 1
        stack_size -= 1

        if low < high:
            pi = particionar(array, low, high)
            c += 1  # Incrementar el contador de iteraciones

            # Agregar los límites del sub-arreglo derecho e izquierdo a la pila
            top += 1
            stack_size += 1
            stack[top] = (low, pi - 1)

            top += 1
            stack_size += 1
            stack[top] = (pi + 1, high)

    print(f"Número de iteraciones: {c}")
    return array

vector = [5, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7,
          3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9,
          7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3,
          1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9,
          7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3,
          1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3,
          1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9,
          7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
          
start = time.time()
sorted_vector = quick_sort(vector)
end = time.time()

print(f"Tiempo: {(end - start) * 1000} ms")
print(vector)
print(sorted_vector)