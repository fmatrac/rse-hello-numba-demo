from rse_hello_numba_demo.core import add_distances
from pint import UnitRegistry

ureg = UnitRegistry()


def test_add_distances():
    result = add_distances(1 * ureg.kilometer, 500 * ureg.meter)
    assert abs(result.magnitude - 1500) < 1e-9


def test_hello_returns_string():
    from rse_hello_numba_demo.core import hello
    assert isinstance(hello(), str)
