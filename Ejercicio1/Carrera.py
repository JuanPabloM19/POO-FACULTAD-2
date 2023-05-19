class Carrera:
    __fecha ="10/01/2002"
    def __init__(self,codigo,nombre,duracion,titulo,grado):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__duracion=duracion
        self.__titulo=titulo
        self.__grado=grado
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getFechaInicio(self):
        return self.__fecha

    def getDuracion(self):
        return self.__duracion
    
    def getTitutlo(self):
        return self.__titulo
    
    def getGrado(self):
        return self.__grado
    
    def __str__(self):
        cadena = self.getCodigo()+" "+self.getNombre() +" "+self.getTitutlo() +" "+self.getDuracion()+" "+self.getGrado()
        return cadena