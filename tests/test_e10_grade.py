"""Tests del ejercicio 10: grade (fronteras y errores)"""
import pytest
from kit_utiles.numbers import grade


@pytest.mark.parametrize(
    "value, letter",
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
    ],
)
def test_grade_bordes(value, letter):
    assert grade(value) == letter


@pytest.mark.parametrize("bad", [-1, 101])
def test_grade_fuera_de_rango(bad):
    with pytest.raises(ValueError):
        grade(bad)


def test_grade_tipo_incorrecto():
    with pytest.raises(TypeError):
        grade(85.0)  # type: ignore[arg-type]
