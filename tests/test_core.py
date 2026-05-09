from rse_hello_numba_demo.core import sum_of_squares, hello


def test_sum_of_squares_known_value():
    # 0^2 + 1^2 + 2^2 + 3^2 = 0 + 1 + 4 + 9 = 14
    assert sum_of_squares(4) == 14.0


def test_sum_of_squares_zero():
    assert sum_of_squares(0) == 0.0


def test_hello_returns_string():
    assert isinstance(hello(), str)
