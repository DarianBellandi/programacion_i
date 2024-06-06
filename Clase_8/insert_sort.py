def insertion_sort(arr):
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
         # Guardamos el valor del elemento actual
        pi = arr[i]
        # Inicializamos j para recorrer la parte ordenada de la lista
        for j in range(i-1,-1,-1):
            if arr[j] > pi:
                arr[j+1] = arr[j]
            if j == 0:
                arr[j] = pi
            

        
        # Movemos los elementos de la parte ordenada que son mayores que key
        # hacia la derecha para hacer espacio para key
        
        # Insertamos key en su posición correcta en la parte ordenada
        

# Ejemplo de uso
arr = [3, 0, 1, 4, 7, 2,5,6]
insertion_sort(arr)
print("Lista ordenada:", arr)        