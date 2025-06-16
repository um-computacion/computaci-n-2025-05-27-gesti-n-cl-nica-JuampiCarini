from entidades.paciente import Paciente
from entidades.turno import Turno
from entidades.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self._paciente = paciente
        self._turnos = []
        self._recetas = []

    def agregar_turno(self, turno: Turno):
        if not isinstance(turno, Turno):
            raise TypeError("Debe ser una instancia de Turno")
        self._turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        if not isinstance(receta, Receta):
            raise TypeError("Debe ser una instancia de Receta")
        self._recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return self._turnos

    def obtener_recetas(self) -> list[Receta]:
        return self._recetas

    def __str__(self) -> str:
        turnos_str = "\n".join(str(turno) for turno in self._turnos) or "Sin turnos."
        recetas_str = "\n".join(str(receta) for receta in self._recetas) or "Sin recetas."
        return (
            f"📋 Historia Clínica de {self._paciente}:\n"
            f"🗓️ Turnos:\n{turnos_str}\n\n"
            f"💊 Recetas:\n{recetas_str}"
        )
