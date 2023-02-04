from datos import *
import random
import numpy as np
#import names #revisar mas tarde la instalación

class Persona():
    def __init__(self):
        self.nombre = darNombre()
        self.estatura = darEstatura(1.45,2.10)
        self.peso = darPeso(40,180)
        self.edad = darEdad(18,90)
    
    def __str__(self) -> str:
        return f"Persona: {self.nombre} | {self.estatura} m | {self.peso} kg | {self.edad} años"

    def __gt__(self,obj):
        return self.edad > obj.edad

    def __lt__(self,obj):
        return self.edad < obj.edad
    
    def __eq__(self,obj):
        return self.edad == obj.edad

def darEstatura(limiteInf, limiteSup):
    return round(random.uniform(limiteInf,limiteSup),2)

def darPeso(limiteInf, limiteSup):
    return round(random.uniform(limiteInf,limiteSup),2)

def darEdad(limiteInf,limiteSup):
    return random.randint(limiteInf,limiteSup)

def darNombre():
    nombre = random.choice(listaHombres)
    apellido1,apellido2 = random.choices(listaApellidos,k=2)

    #apellido1 = random.choice(listaApellidos)
    #apellido2 = random.choice(listaApellidos)
    
    return f"{nombre} {apellido1} {apellido2}"

#--------------------------------------------------#

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

#main
if __name__ == "__main__":
    #obj1 = Persona()
    #obj2 = Persona()
    #if obj1 > obj2:
        #print("obj1 > obj2")
    #else:
        #print("obj1 < obj2")
    #print(f'obj1 -> {obj1}')
    #print(f'obj2 -> {obj2}')
    pass
    