from qiskit import QuantumCircuit

from my_quantum.runner import QuantumRunner


def deutsch_circuit(function: QuantumCircuit) -> QuantumCircuit:
    """Insert the provided circuit within a Deutsch algorithm.

    The new circuit can be run and evaluated, returning 0 if the function is
    constant and 1 if it isn't.

    The input function remains unchanged.

    Implementation written using the following reference :
    https://quantum.cloud.ibm.com/learning/fr/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/deutsch-algorithm

    Params:
        function (QuantumCircuit): the function to perform on

    Returns:
        A circuit performing the Deutsch algorithm over the provided function.

    See also:
        deutsch_algorithm: evaluate the circuit directly and interprets the
                           result as a Python native boolean
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


def deutsch_algorithm(function: QuantumCircuit, runner: QuantumRunner) -> bool:
    """Perform a Deutsch algorithm over the provided quantum circuit.

    The function returns True if the provided function is a constant, always
    returning the same value. Otherwise, it returns False.

    We define a constant function as a quantum operation that returns the same
    quantum state as output, regardless of the state of the input qubits is.

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
    """

    circuit = deutsch_circuit(function)

    run = runner.run(circuit, shots=1, memory=True)
    result = run.result()
    measures = result.get_memory()

    output_bit: str = measures[0]

    return int(output_bit) == 0


__all__ = ["deutsch_algorithm", "deutsch_circuit"]
