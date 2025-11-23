from qiskit import QuantumCircuit


def deutsch_jozsa_circuit(function: QuantumCircuit) -> QuantumCircuit:
    """Wrap the function inside the Deutsch Jozsa algorithm.

    The Deutsch-Josza algorithm either returns an all-0 quantum state if the
    function is constant, or one with an equal amount of zeros and ones if it
    is balanced.

    This function also goes under the promise the function is EITHER constant
    or balanced. Unbalanced functions are not handled.

    Implementation written using the following reference :
    https://quantum.cloud.ibm.com/learning/fr/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/deutsch-jozsa-algorithm#deutsch-jozsa-avec-qiskit

    Params:
        function (QuantumCircuit): the function to perform the algorithm on

    Returns:
        A circuit representing the Deutsch-Josza quantum alrgorithm operated on
        the provided function

    See also:
        deutsch_jozsa_algorithm: directly evaluates the circuit and interpret
                                 the result using a Python native boolean
        deutsch_circuit: simplified version of the circuit for functions on
                         only one input
    """

    n = function.num_qubits - 1

    circuit = QuantumCircuit(n + 1, n)

    circuit.x(n)
    circuit.h(range(n + 1))

    circuit.barrier()
    circuit.compose(function, inplace=True)
    circuit.barrier()

    circuit.h(range(n))
    circuit.measure(range(n), range(n))

    return circuit


__all__ = ["deutsch_jozsa_circuit"]
