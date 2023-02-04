import random
import time

def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Último elemento no necesita ser comprobado
        for j in range(0, n-i-1):
            # Intercambiar elementos si están en orden equivocado
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def crear_datos(n:int):
    arr = list()
    for i in range(n):
        arr.append(random.randint(0,10000))
    return arr

#arr = [64, 34, 25, 12, 22, 11, 90]
arr = crear_datos(10000)
inicio = time.time()
print("Lista ordenada es:",bubble_sort(arr))
fin = time.time()
print(fin-inicio)