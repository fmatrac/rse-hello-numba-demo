# rse-hello-numba-demo

Demo projektu używającego biblioteki Numba do przyspieszania obliczeń przez kompilację JIT.

## Przykład użycia

```python
from rse_hello_numba_demo import hello
print(hello())
```

## Instalacja

```bash
pip install rse-hello-numba-demo
```

## API

### `hello()`

Zwraca string z wynikiem przykładowego obliczenia JIT.

### `sum_of_squares(n)`

Oblicza sumę kwadratów `0² + 1² + ... + (n-1)²` przy użyciu Numba `@njit`.

```python
from rse_hello_numba_demo import sum_of_squares

result = sum_of_squares(1_000_000)
print(result)  # 333332833333500000.0
```
