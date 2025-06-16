from datetime import datetime

class Turno:
    def __init__(self, paciente, medico, fecha_hora: datetime):
        self._paciente = paciente
        self._medico = medico
        self._fecha_hora = fecha_hora

    def obtener_fecha_hora(self) -> datetime:
        return self._fecha_hora

    def obtener_medico(self):  
        return self._medico

    def __str__(self) -> str:
        return f"Turno: {self._fecha_hora.strftime('%d/%m/%Y %H:%M')} - Paciente: {self._paciente} - Médico: {self._medico}"
