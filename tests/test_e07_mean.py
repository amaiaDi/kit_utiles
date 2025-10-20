"""Tests del ejercicio 7: mean (errores y cálculo)"""
import pytest
from kit_utiles.numbers import mean


def test_mean_ok():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_vacio():
    with pytest.raises(ValueError, match="empty sequence"):
        mean([])
