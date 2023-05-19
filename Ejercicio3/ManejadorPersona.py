from claseInscripcion import Inscripcion
from clasePersona import Persona
from claseTaller import TallerCapacitacion

class ManejadorPersonas:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        self._personas.append(persona)

    def buscar_persona(self, dni):
        for persona in self._personas:
            if persona.get_dni() == dni:
                return persona
        return None