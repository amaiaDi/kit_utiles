"""Tests del ejercicio 3: is_leap_year (parametrización)"""
import pytest
from src.numbers import is_leap_year


@pytest.mark.parametrize(
    "year, expected",
    [
        (2000, True),   # divisible por 400
        (1900, False),  # divisible por 100 (no bisiesto)
        (2024, True),   # divisible por 4
        (2023, False),  # no bisiesto
    ],
)
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected
