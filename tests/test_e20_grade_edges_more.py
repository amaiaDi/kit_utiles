# Cubre bordes adicionales. Fallará si grade acepta float o no valida rango.
import pytest
from kit_utiles.numbers import grade

@pytest.mark.parametrize("val,letter", [(100,"A"), (90,"A"), (89,"B"), (80,"B"), (79,"C"), (70,"C"), (69,"D"), (60,"D"), (59,"F"), (0,"F")])
def test_grade_bordes(val, letter):
    assert grade(val) == letter

def test_grade_tipo_float():
    with pytest.raises(TypeError):
        grade(90.0)

def test_grade_fuera_rango():
    with pytest.raises(ValueError):
        grade(-1)
    with pytest.raises(ValueError):
        grade(101)
