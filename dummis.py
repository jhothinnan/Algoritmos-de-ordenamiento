from generador import *
from mergeSortEdison import *
from quickSortEdison import *

def crearDatos(cantidad):
    try:    
        if cantidad > 0:
            lista = list()
            for item in range (cantidad):
                lista.append(Persona())
            return lista
    except:
        return None

def verLista(lista):
    i = 1
    for item in lista:
        print(f'({i}) {item}')
        i+=1

if __name__ == "__main__":
    datos = crearDatos(int(input("¿Cuantos datos?")))
    #datos = [4,9,1,78,7,-8,5,4,78]
    #datos = ['camisa','vaca','carro','avion']
    verLista(datos)

    print("-"*20)
    datosOrd = quickSort(datos)
    verLista(datosOrd)