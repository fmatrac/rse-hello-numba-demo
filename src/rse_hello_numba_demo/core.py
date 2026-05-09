from numba import njit
import numpy as np


@njit
def sum_of_squares(n):  # pragma: no cover
    """Compute sum of squares 0^2 + 1^2 + ... + (n-1)^2 using JIT compilation."""
    total = 0.0
    for i in range(n):
        total += i * i
    return total


def hello():
    result = sum_of_squares(1_000_000)
    return f"Hello! Sum of squares up to 1,000,000 = {result:.0f}"
