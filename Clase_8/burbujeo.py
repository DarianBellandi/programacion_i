import time
c = 0
def bubble_sort(array):
    global c
    for i in range(0,len(array)-1):
        c += 1
        #print(f"{i}")
        for j in range(i+1,len(array)):
            #print(f"\t{j}")
            if array[i] > array[j]:
                auxiliar = array[i]
                array[i] = array[j]
                array[j] = auxiliar
        

# Ejemplo de uso
vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7]

start = time.time()
bubble_sort(vector)
end = time.time()
print(f"Tiempo: {(end - start)*1000}")
print(f"cantidad iteraciones: {c}")
print(len(vector))