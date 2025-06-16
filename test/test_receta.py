import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from entidades.receta import Receta


class PacienteMock:
    def __str__(self):
        return "Ana Gómez (DNI: 12345678)"

class MedicoMock:
    def __str__(self):
        return "Dr. Juan Perez - Cardiología (Matrícula: 12345)"

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = PacienteMock()
        self.medico = MedicoMock()
        self.medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.fecha = datetime(2025, 6, 16)
        self.receta = Receta(self.paciente, self.medico, self.medicamentos, self.fecha)

    def test_str(self):
        esperado = ("Receta (16/06/2025): Paracetamol, Ibuprofeno - Paciente: Ana Gómez (DNI: 12345678) - "
                    "Médico: Dr. Juan Perez - Cardiología (Matrícula: 12345)")
        self.assertEqual(str(self.receta), esperado)

if __name__ == "__main__":
    unittest.main()