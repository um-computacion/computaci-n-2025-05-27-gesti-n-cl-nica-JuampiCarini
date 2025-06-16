import unittest
from datetime import datetime
import sys
import os

# Agregar el path del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entidades.historia_clinica import HistoriaClinica
from entidades.turno import Turno
from entidades.receta import Receta

# Mock paciente
class PacienteMock:
    def __str__(self):
        return "Paciente Mock"

# Mock turno
class TurnoMock(Turno):
    def __init__(self, paciente, medico, fecha_hora):
        super().__init__(paciente, medico, fecha_hora)

    def __str__(self):
        return "Turno Mock"

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = PacienteMock()
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno_y_receta(self):
        turno = TurnoMock(self.paciente, "Medico1", datetime.now())
        receta = Receta(
            paciente=self.paciente,
            medico="Dr. House",
            medicamentos=["Ibuprofeno", "Paracetamol"],
            fecha=datetime(2025, 6, 16)
        )

        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)

        self.assertIn(turno, self.historia.obtener_turnos())
        self.assertIn(receta, self.historia.obtener_recetas())

    def test_str(self):
        turno = TurnoMock(self.paciente, "Medico1", datetime.now())
        receta = Receta(
            paciente=self.paciente,
            medico="Dr. House",
            medicamentos=["Ibuprofeno", "Paracetamol"],
            fecha=datetime(2025, 6, 16)
        )

        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)

        salida = str(self.historia)
        self.assertIn("Paciente Mock", salida)
        self.assertIn("Turno Mock", salida)
        self.assertIn("Dr. House", salida)

if __name__ == "__main__":
    unittest.main()