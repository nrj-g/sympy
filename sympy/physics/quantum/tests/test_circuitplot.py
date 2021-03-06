from sympy.physics.quantum.circuitplot import labler
from sympy.physics.quantum.gate import CNOT, H, X, Z, SWAP, CGate, S, T
from sympy.external import import_module
from sympy.utilities.pytest import skip

mpl = import_module('matplotlib')

def test_labler():
    """Test the labler utility"""
    assert labler(2) == ['q_1', 'q_0']
    assert labler(3,'j') == ['j_2', 'j_1', 'j_0']

def test_cnot():
    """Test a simple cnot circuit. Right now this only makes sure the code doesn't
    raise an exception, and some simple properties
    """
    if not mpl:
        skip("matplotlib not installed")
    else:
        from sympy.physics.quantum.circuitplot import CircuitPlot

    c = CircuitPlot(CNOT(1,0),2,labels=labler(2))
    assert c.ngates == 2
    assert c.nqubits == 2
    assert c.labels == ['q_1', 'q_0']

    c = CircuitPlot(CNOT(1,0),2)
    assert c.ngates == 2
    assert c.nqubits == 2
    assert c.labels == []

def test_ex1():
    if not mpl:
        skip("matplotlib not installed")
    else:
        from sympy.physics.quantum.circuitplot import CircuitPlot

    c = CircuitPlot(CNOT(1,0)*H(1),2,labels=labler(2))
    assert c.ngates == 2
    assert c.nqubits == 2
    assert c.labels == ['q_1', 'q_0']

def test_ex4():
    if not mpl:
        skip("matplotlib not installed")
    else:
        from sympy.physics.quantum.circuitplot import CircuitPlot

    c = CircuitPlot(SWAP(0,2)*H(0)* CGate((0,),S(1)) *H(1)*CGate((0,),T(2))\
                    *CGate((1,),S(2))*H(2),3,labels=labler(3,'j'))
    assert c.ngates == 7
    assert c.nqubits == 3
    assert c.labels == ['j_2', 'j_1', 'j_0']
