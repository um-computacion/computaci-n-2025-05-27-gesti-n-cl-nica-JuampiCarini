class Paciente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: str):
        self._dni = dni
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self._dni

    def __str__(self) -> str:
        return f"{self._nombre} (DNI: {self._dni})"
