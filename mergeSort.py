import random
import time

def merge(arr1, arr2):
    arr3 = list()
    while (len(arr1) > 0 and len(arr2) > 0):
        if(arr1[0]>arr2[0]):
            arr3.append(arr2[0])
            arr2.pop(0)
        else:
            arr3.append(arr1[0])
            arr1.pop(0)

    while (len(arr1) > 0):
        arr3.append(arr1[0])
        arr1.pop(0)

    while (len(arr2) > 0):
        arr3.append(arr2[0])
        arr2.pop(0)
    
    return arr3

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1,arr2)

def crear_datos(n:int):
    arr = list()
    for i in range(n):
        arr.append(random.randint(0,10000))
    return arr

arr = crear_datos(10000)
inicio = time.time()
print("Lista ordenada es:",merge_sort(arr))
fin = time.time()
print(fin-inicio)