import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from entidades.paciente import Paciente  

class TestPaciente(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Ana Gómez", "1990-05-15")

    def test_obtener_dni(self):
        self.assertEqual(self.paciente.obtener_dni(), "12345678")

    def test_str(self):
        esperado = "Ana Gómez (DNI: 12345678)"
        self.assertEqual(str(self.paciente), esperado)

if __name__ == "__main__":
    unittest.main()