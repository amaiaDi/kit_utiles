import pytest
from kit_utiles.numbers import is_leap_year

def test_is_leap_year_century_rules():
    assert is_leap_year(2000) is True  # divisible por 400
    assert is_leap_year(1900) is False # divisible por 100 pero no por 400

def test_is_leap_year_type_error():
    with pytest.raises(TypeError):
        is_leap_year(True)  # tipo no int aceptado como bool -> debe rechazarse si lo haces así
