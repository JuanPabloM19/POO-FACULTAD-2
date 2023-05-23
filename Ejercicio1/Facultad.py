class Facultad:
    
    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carreras=[]
    
    def agregaCarrera(self,codigo,nombre,duracion,titulo,grado):
        from Carrera import Carrera
        obj=Carrera(codigo, nombre, duracion, titulo,grado)
        self.__carreras.append(obj)
    
    def getCarreras(self):
        for i in self.__carreras:
            print(i)
    def cantCarreras(self):
        return len(self.__carreras)
            
    def getNombre(self):
        return self.__nombre
    
    def buscaCarrera(self,carrera):
        i =0
        while i < len(self.__carreras) and self.__carreras[i].getNombre() != carrera:
            i += 1
            
        if i < len(self.__carreras):
            bandera=True
        else:
            bandera=False
            
        return bandera
    def codigoCarrera(self,carrera):
        i =0
        while i < len(self.__carreras) and self.__carreras[i].getNombre() != carrera:
            i += 1
            
        if i < len(self.__carreras):
            cadena= str(self.__carreras[i].getNombre())
        else:
            cadena= "CMAMO"
            
        return cadena
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self):
        return self.__localidad
    
    def getCodigo(self):
        return self.__codigo
    
    def getTelefono(self):
        return self.__telefono
    
    def __str__(self):
        cadena= self.getNombre()+" "+self.getDireccion+" "+self.getLocalidad()+" "+self.getTelefono()
        return cadena