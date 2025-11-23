from qiskit import QuantumCircuit


def deutsch_circuit(function: QuantumCircuit) -> QuantumCircuit:
    """Wraps the provided function within a Deutsch algorithm circuit.

    The new circuit can be run and evaluated, returning 0 if the function is
    constant and 1 if it isn't.

    This is a simplified circuit of the Deutsch-Jozsa algorithm, which only
    operates on functions of one single input. For other types of functions,
    use deutsch_jozsa_circuit instead.

    Implementation written using the following reference :
    https://quantum.cloud.ibm.com/learning/fr/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/deutsch-algorithm

    Params:
        function (QuantumCircuit): the function to perform the algorithm on

    Returns:
        A circuit performing the Deutsch algorithm over the provided function.
        The circuit MUST be of size 2, with one input and one output registers

    See also:
        deutsch_algorithm: evaluate the circuit directly and interprets the
                           result as a Python native boolean
        deutsch_jozsa_circuit: generalized form of the algorithm
    """

    assert function.num_qubits == 2, \
        "deutsch_circuit can only work on functions of size 2. use " \
        "deutsch_jozsa_circuit instead"

    all_qubits = slice(0, 1)
    circuit = QuantumCircuit(
        2, 1, name=f"Deutsch algorithm over {function.name}"
    )

    circuit.x(1)
    circuit.h(all_qubits)

    circuit.barrier()
    circuit.compose(function, inplace=True)
    circuit.barrier()

    circuit.h(all_qubits)
    circuit.measure(all_qubits, all_qubits)

    return circuit


__all__ = ["deutsch_circuit"]
