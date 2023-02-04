def mergeSort(datos):
    if len(datos) <= 1:
        return datos
    if len(datos) == 2:
        return sorted(datos)
    else:
        mitadDatos = len(datos)//2
        return merge(mergeSort(datos[:mitadDatos]),mergeSort(datos[mitadDatos:]))

def merge(datosA,datosB):
    p1,p2 = 0,0
    resutado = list()
    while(p1 < len(datosA) and p2 < len(datosB)):
        if datosA[p1] < datosB[p2]:
            resutado.append(datosA[p1])
            p1 +=1
        else:
            resutado.append(datosB[p2])
            p2 +=1
    resutado += datosA[p1:]+datosB[p2:]
    return resutado