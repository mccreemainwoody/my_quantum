from typing import Any, Protocol

from qiskit import QuantumCircuit
from qiskit.providers import Job


class QuantumRunner(Protocol):
    """Expected definition of a Quantum runtime.

    Such runtime may be, for example, the Quantum simulator qiskit_aer, or
    the IBM Quantum Runtime.
    """

    def run(self, circuit: QuantumCircuit, **run_options: Any) -> Job:
        """Start a Quantum Circuit.

        Return the computation result as a job, proccessing the computation
        asynchronously.
        """
        ...
