import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from entidades.turno import Turno

# Mocks simples
class PacienteMock:
    def __str__(self):
        return "Ana Gómez (DNI: 12345678)"

class MedicoMock:
    def __str__(self):
        return "Dr. Juan Perez - Cardiología (Matrícula: 12345)"

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = PacienteMock()
        self.medico = MedicoMock()
        self.fecha_hora = datetime(2025, 6, 16, 14, 30)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_str(self):
        esperado = ("Turno: 16/06/2025 14:30 - Paciente: Ana Gómez (DNI: 12345678) - "
                    "Médico: Dr. Juan Perez - Cardiología (Matrícula: 12345)")
        self.assertEqual(str(self.turno), esperado)

if __name__ == "__main__":
    unittest.main()