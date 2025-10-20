"""Tests del ejercicio 1: sum_list"""
from kit_utiles.numbers import sum_list


def test_sum_list_suma_correcta():
    # Arrange
    datos = [1, 2, 3, 4]
    # Act
    res = sum_list(datos)
    # Assert
    assert res == 10


def test_sum_list_lista_vacia():
    assert sum_list([]) == 0
