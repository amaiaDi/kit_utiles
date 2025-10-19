"""Tests del ejercicio 2: unique_sorted"""
from src.numbers import unique_sorted


def test_unique_sorted_enteros():
    assert unique_sorted([3, 1, 2, 3, 2]) == [1, 2, 3]


def test_unique_sorted_cadenas():
    assert unique_sorted(["b", "a", "b"]) == ["a", "b"]
