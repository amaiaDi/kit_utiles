"""Tests del ejercicio 5: word_count (fixtures)"""
import pytest
from kit_utiles.strings import word_count


@pytest.fixture
def texto():
    return "Hola, hola... ¿Qué tal? Tal vez bien: hola!"


def test_word_count_basico(texto):
    res = word_count(texto)
    assert res["hola"] == 3
    assert res["tal"] == 2
    assert res["que"] == 1
    assert "inexistente" not in res
