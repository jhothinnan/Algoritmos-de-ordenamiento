from mergeSortEdison import *
from quickSortEdison import *
from generador import *
from time import time

def medir(metodo,datos):
    #Llamar ordenamiento
    start_time = time()
    if metodo == "MergeSort":
        start_time = time()
        datosOrd = mergeSort(datos)
    elif metodo == "QuickSort":
        start_time = time()
        datosOrd = quickSort(datos)

    stop_time = time()
    total_time = stop_time-start_time
    print(f'{metodo} Se demoro: {total_time} segundos.')

def prueba():
    cantidad = int(input("¿Cuantos datos desea generar?"))
    datos = crearDatos(cantidad)
    medir('MergeSort',datos)
    medir('QuickSort',datos)
    
if __name__ == '__main__':
    prueba()
