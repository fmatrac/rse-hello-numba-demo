# rse-hello-numba-demo

A hello-world Python project demonstrating JIT-accelerated computing with [Numba](https://numba.readthedocs.io/).

## Installation

```bash
pip install rse-hello-numba-demo
```

## Usage

```python
from rse_hello_numba_demo import hello, sum_of_squares

print(hello())
# Hello! Sum of squares up to 1,000,000 = 333332833333500000

result = sum_of_squares(10)
print(result)  # 285.0
```

## Development

```bash
pip install -e ".[dev]"
pytest --cov=rse_hello_numba_demo
```

## License

MIT
