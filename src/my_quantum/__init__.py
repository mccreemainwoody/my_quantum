"""Simple library containing various basic quamtum algorithms."""

from .runner import QuantumRunner
from .deutsch import (
    deutsch_algorithm,
    deutsch_circuit,
)
from .deutsch_jozsa import (
    deutsch_jozsa_algorithm,
    deutsch_jozsa_circuit,
)


__all__ = [
    "deutsch_algorithm", 
    "deutsch_circuit",
    "deutsch_jozsa_algorithm",
    "deutsch_jozsa_circuit",
    "QuantumRunner",
]
