import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from entidades.medico import Medico 

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("12345", "Juan Perez", "Cardiología")

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "12345")

    def test_str(self):
        esperado = "Juan Perez - Cardiología (Matrícula: 12345)"
        self.assertEqual(str(self.medico), esperado)

if __name__ == "__main__":
    unittest.main()