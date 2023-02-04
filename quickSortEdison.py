def quickSort(datos):
    if len(datos) <= 1:
        return datos
    else:
        pivote = datos[len(datos)//2]
        datosMenores = [item for item in datos if item < pivote]
        datosMayores = [item for item in datos if item > pivote]
        datosIguales = [item for item in datos if item == pivote]
        return quickSort(datosMenores) + datosIguales + quickSort(datosMayores)