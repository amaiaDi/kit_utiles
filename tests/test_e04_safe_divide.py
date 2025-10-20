"""Tests del ejercicio 4: safe_divide (excepciones)"""
import pytest
from kit_utiles.numbers import safe_divide


def test_safe_divide_ok():
    assert safe_divide(10, 2) == 5


def test_safe_divide_zero():
    with pytest.raises(ValueError, match="division by zero"):
        safe_divide(1, 0)


def test_safe_divide_tipo_invalido():
    with pytest.raises(TypeError):
        safe_divide("3", 2)  # type: ignore[arg-type]
