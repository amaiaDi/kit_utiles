# Si mean no lanza ValueError en secuencia vacía, fallará el test.
# Si hay error de precisión grueso, también se notará.
import math
import pytest
from kit_utiles.numbers import mean

def test_mean_vacia_error():
    with pytest.raises(ValueError):
        mean([])

def test_mean_precision_simple():
    assert math.isclose(mean([0.1, 0.2, 0.3]), 0.2, rel_tol=1e-9, abs_tol=1e-12)
