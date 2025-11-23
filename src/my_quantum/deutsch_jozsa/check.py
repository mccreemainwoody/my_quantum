from my_quantum import QuantumRunner
from qiskit import QuantumCircuit

from .circuit import deutsch_jozsa_circuit


def deutsch_jozsa_algorithm(function: QuantumCircuit, runner: QuantumRunner) -> bool:
    """Return whether a quantum function is constant or balanced.

    This is a generalization of the Deutsch algorthm, which can work with
    function working on any amount of qubits.

    This function also goes under the promise the function is EITHER constant
    or balanced. Unbalanced functions are not handled.

    Params:
        function (QuantumCircuit): the function to perform the algorithm on
        runner (QuantumRunner): the runner to use to run the circuit

    Returns:
        True if the function is constant, False otherwise.
    """

    circuit = deutsch_jozsa_circuit(function)

    job = runner.run(circuit, shots=1, memory=True)
    result = job.result()
    measurements = result.get_memory()

    output_bit: str = measurements[0]

    return "1" not in output_bit 



__all__ = ["deutsch_jozsa_algorithm"]
