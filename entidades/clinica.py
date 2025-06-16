from datetime import datetime

from exeptiones import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

from entidades.historia_clinica import HistoriaClinica
from entidades.receta import Receta
from entidades.turno import Turno


class Clinica:
    def __init__(self):
        self._pacientes = {}
        self._medicos = {}
        self._turnos = []
        self._historias_clinicas = {}

    def agregar_paciente(self, paciente):
        self._pacientes[paciente.obtener_dni()] = paciente
        self._historias_clinicas[paciente.obtener_dni()] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        self._medicos[medico.obtener_matricula()] = medico

    def agendar_turno(self, dni: str, matricula: str, fecha_hora: datetime):
        if dni not in self._pacientes:
            raise PacienteNoExisteError()
        if matricula not in self._medicos:
            raise MedicoNoExisteError()

        for turno in self._turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and
                    turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoDuplicadoError()

        turno = Turno(self._pacientes[dni], self._medicos[matricula], fecha_hora)
        self._turnos.append(turno)
        self._historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        if dni not in self._pacientes:
            raise PacienteNoExisteError()
        if matricula not in self._medicos:
            raise MedicoNoExisteError()

        receta = Receta(self._pacientes[dni], self._medicos[matricula], medicamentos, datetime.now())
        self._historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str):
        return self._historias_clinicas[dni]

    def obtener_turnos(self) -> list:
        return self._turnos
    def obtener_pacientes(self) -> list:
        return list(self._pacientes.values())
    def obtener_medicos(self) -> list:
        return list(self._medicos.values())
    