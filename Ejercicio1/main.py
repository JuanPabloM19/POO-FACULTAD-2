from ManejadorFacultades import ManejadorFacultades

if __name__ == "__main__":
    lista=ManejadorFacultades()
    lista.carga()
    
    print("1: Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad. ")
    print("2: Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta. ")
    print("Ingresar 0 para finalizar.")
    
    cod=int(input("Ingrese la opcion a realizar: "))
    
    while cod!=0:
        
        if cod ==1:
            codigo=int(input("Ingresar el codigo a buscar: "))
            lista.buscaCodigo(codigo)
        elif cod==2:
            nombre=input("Ingresar el nombre de la carrera a buscar: ")
            lista.buscaNombreCarrera(nombre)
        else: 
            cod=int(input("Ingresar un codigo valido: "))
            
        print("1: Para buscar una facultad respecto a su codigo, mostrando las carreras con su duracion. ")
        print("2: Ingresar un nombre de una carrera para buscarla, mostrando la facultad y su direccion. ")
        
        cod=int(input("Ingrese la opcion a realizar: "))