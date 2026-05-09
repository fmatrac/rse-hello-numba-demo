from pint import UnitRegistry

ureg = UnitRegistry()


def add_distances(d1, d2):
    """Add two distances with units."""
    return (d1 + d2).to("meter")


def hello():
    result = add_distances(1 * ureg.kilometer, 500 * ureg.meter)
    return f"Hello! 1 km + 500 m = {result}"
