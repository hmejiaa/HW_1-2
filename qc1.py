from qiskit import QuantumCircuit,  QuantumRegister
from qiskit.quantum_info import Statevector
from math import pi # you'll need this

def example_not():
    """ This is an example that passes a test of the not gate (x gate)

    Args: 
        None
    """
    qr=QuantumRegister(1)
    qc=QuantumCircuit(qr)
    qc.x(qr[0])
    return Statevector.from_instruction(qc)

def hadamard():
    """ Implement a function that returns the state vector after applying
        the hadamard gate (h)

    Args: 
        None
    """
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    qc.h(q[0])

    return Statevector.from_instruction(qc)

def one_state():
    """ Implement a function that returns the state vector after applying
        the phase gate (z)

    Args: 
        None
    """
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    qc.z(q[0])
    qc.x(q[0])
    
    return Statevector.from_instruction(qc)


def phase():
    """ Implement a function that returns the state vector corresponding to the test
    test_phase, in other words,  0|0⟩-1|1⟩

    Args: 
        None
    """
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    qc.x(q[0])
    qc.z(q[0])
    
    return Statevector.from_instruction(qc)


def figure_it_out_1():
    """ Implement a function that returns the state vector corresponding to 
        √2/2|0⟩ - √2/2|1⟩ , also known as |−⟩ 

    Args: 
        None
    """
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    qc.h(q[0])
    qc.z(q[0])
    
    return Statevector.from_instruction(qc)


def figure_it_out_2():
    """ Implement a function that returns the state vector to pass the
        test test_figure_it_out_2, USING ONLY GATES. In other words,
        θ=π/2 and φ=π/4 
        hint: do this with two gates
        
    Args: 
        None
    """
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    qc.h(q[0])
    qc.t(q[0])
    
    return Statevector.from_instruction(qc)


def figure_it_out_3():
    """ Implement a function that returns the state vector to pass the
        test test_figure_it_out_3, USING ONLY GATES. In other words, 
        θ=π/2 and φ=π/16  
        hint: do this with two gates
        
    Args: 
        None
    """
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    qc.u(pi/2, pi/16, 1, q[0])
    
    return Statevector.from_instruction(qc)


def figure_it_out_4():
    """ Implement a function that returns the state vector to pass the
        test test_figure_it_out_4, USING ONLY GATES. In other words, 
        θ=π/7 and φ=π/5
        hint: do this with one gate!
        
    Args: 
        None
    """
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    qc.u(pi/7, pi/5, 1, q[0])
    
    return Statevector.from_instruction(qc)


if __name__ == '__main__':
    print(example_not())
    print(hadamard())
    print(one_state())
    print(phase())
    print(figure_it_out_1())
    print(figure_it_out_2())
    print(figure_it_out_3())
    print(figure_it_out_4())

    