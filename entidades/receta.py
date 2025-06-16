from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos: list[str], fecha: datetime):
        self._paciente = paciente
        self._medico = medico
        self._medicamentos = medicamentos
        self._fecha = fecha

    def __str__(self) -> str:
        return f"Receta ({self._fecha.strftime('%d/%m/%Y')}): {', '.join(self._medicamentos)} - Paciente: {self._paciente} - Médico: {self._medico}"
