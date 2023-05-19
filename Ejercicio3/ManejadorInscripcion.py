from claseInscripcion import Inscripcion
from clasePersona import Persona
from claseTaller import TallerCapacitacion

class ManejadorInscripciones:
    def __init__(self):
        self._inscripciones = []

    def agregar_inscripcion(self, inscripcion):
        self._inscripciones.append(inscripcion)

    def buscar_inscripcion(self, dni):
        for inscripcion in self._inscripciones:
            if inscripcion.get_persona().get_dni() == dni:
                return inscripcion
        return None

    def listar_inscriptos(self, idTaller):
        inscriptos = []
        for inscripcion in self._inscripciones:
            if inscripcion.get_taller().get_idTaller() == idTaller:
                inscriptos.append(inscripcion)
        return inscriptos

    def guardar_inscripciones(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            for inscripcion in self._inscripciones:
                pago_str = "1" if inscripcion.get_pago() else "0"
                f.write(f"{inscripcion.get_persona().get_dni()},{inscripcion.get_taller().get_idTaller()},{inscripcion.get_fechaInscripcion()},{pago_str}\n")