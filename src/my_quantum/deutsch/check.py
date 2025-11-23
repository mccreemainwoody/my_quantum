from my_quantum import QuantumRunner
from qiskit import QuantumCircuit

from .circuit import deutsch_circuit


def deutsch_algorithm(function: QuantumCircuit, runner: QuantumRunner) -> bool:
    """Perform a Deutsch algorithm over the provided quantum circuit.

    The function returns True if the provided function is a constant (always
    returning the same value regardless on the input). Otherwise, it returns
    False.

    For functions of more than one input, see deutsch_jozsa_algorithm instead.

    Implementation written using the following reference :
    https://quantum.cloud.ibm.com/learning/fr/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/deutsch-algorithm

    Params:
        function (QuantumCircuit): the function to perform on
        runner (QuantumRUnner): runner to run the circuit with

    Returns:
        True if function is constant. False otherwise

    See also:
        deutsch_circuit: simply create the circuit without evaluating it.
                         this function depends directly on this one
        deutsch_jozsa_algorithm: generalized form of the algorithm
    """

    circuit = deutsch_circuit(function)

    run = runner.run(circuit, shots=1, memory=True)
    result = run.result()
    measurements = result.get_memory()

    output_bit: str = measurements[0]

    return int(output_bit) == 0


__all__ = ["deutsch_algorithm"]
