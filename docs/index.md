# rse-hello-numba-demo

Demo projektu używającego biblioteki Pint.

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

Zwraca string z przykładem dodawania odległości.

### `add_distances(d1, d2)`

Dodaje dwie odległości z jednostkami i zwraca wynik w metrach.

```python
from rse_hello_numba_demo import add_distances
from pint import UnitRegistry

ureg = UnitRegistry()
result = add_distances(1 * ureg.kilometer, 500 * ureg.meter)
print(result)  # 1500.0 meter
```
