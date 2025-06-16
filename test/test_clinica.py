import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from entidades.clinica import Clinica
from entidades.turno import Turno
from entidades.receta import Receta
from exeptiones import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class PacienteMock:
    def obtener_dni(self):
        return "12345678"

class MedicoMock:
    def obtener_matricula(self):
        return "M001"

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = PacienteMock()
        self.medico = MedicoMock()
        self.fecha = datetime(2025, 6, 17, 10, 0)

        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_exitoso(self):
        self.clinica.agendar_turno("12345678", "M001", self.fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_paciente_no_existe(self):
        with self.assertRaises(PacienteNoExisteError):
            self.clinica.agendar_turno("00000000", "M001", self.fecha)

    def test_medico_no_existe(self):
        with self.assertRaises(MedicoNoExisteError):
            self.clinica.agendar_turno("12345678", "X999", self.fecha)

    def test_turno_duplicado(self):
        self.clinica.agendar_turno("12345678", "M001", self.fecha)
        with self.assertRaises(TurnoDuplicadoError):
            self.clinica.agendar_turno("12345678", "M001", self.fecha)

if __name__ == "__main__":
    unittest.main()