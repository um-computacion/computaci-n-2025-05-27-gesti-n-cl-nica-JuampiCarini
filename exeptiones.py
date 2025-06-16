"""Custom exception classes for the entidades module."""

class PacienteNoExisteError(Exception):
    """Exception raised when a patient does not exist."""

class MedicoNoExisteError(Exception):
    """Exception raised when a doctor does not exist."""

class TurnoDuplicadoError(Exception):
    """Exception raised when a duplicate appointment is found."""
