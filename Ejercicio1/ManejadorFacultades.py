import csv
from Facultad import Facultad

class ManejadorFacultades:
    def __init__(self):
        self.__lista=[]
        
    def carga(self):
        arch=open("Facultades.csv", encoding="utf-8")
        rea=csv.reader(arch,delimiter=",")
        bandera=True
        i=0
        for fila in rea:
           if bandera:
               facu=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
               self.__lista.append(facu)
               bandera=False
               i=int(fila[0])
           else:    
               if i == int(fila[0]):
                   self.__lista[len(self.__lista)-1].agregaCarrera(fila[1],fila[2],fila[3],fila[4],fila[5])
               else:    
                   i = int(fila[0])
                   facu=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                   self.__lista.append(facu)
                   
    def buscaCodigo(self,codigo):
        i=0
        while int(self.__lista[i].getCodigo()) != codigo and i<len(self.__lista):
            i +=1
        if i < len(self.__lista):
           self.__lista[i].getNombre()
           self.__lista[i].getCarreras()
        else:
            print("No se encontro la facultad con el codigo ingresado")
            
    def buscaNombreCarrera(self,nombreCarrera):
        i = 0
        bandera = True
        while i < len(self.__lista) and bandera:
            if self.__lista[i].buscaCarrera(nombreCarrera):
                bandera=False
            else:
                i += 1
        if i<len(self.__lista):
            print(f"La Facultad codigo: {self.__lista[i].getCodigo()} que se llama: {self.__lista[i].getNombre()} de localidad: {self.__lista[i].getLocalidad()} con el codigo de carrera: {self.__lista[i].codigoCarrera(nombreCarrera)}")
        else:
            print("No se encontro la carrera a buscar")
            