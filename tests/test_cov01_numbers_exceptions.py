import pytest
from kit_utiles.numbers import clamp, safe_divide, mean, grade

def test_clamp_low_mayor_high():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)

def test_safe_divide_zero_lanza():
    with pytest.raises(ValueError, match="division by zero"):
        safe_divide(1, 0)

def test_safe_divide_tipo_invalido():
    with pytest.raises(TypeError):
        safe_divide("1", 2)

def test_mean_vacio_mensaje():
    with pytest.raises(ValueError, match="empty sequence"):
        mean([])

def test_grade_tipo_float_y_fuera_rango():
    with pytest.raises(TypeError):
        grade(95.5)
    with pytest.raises(ValueError):
        grade(-5)
