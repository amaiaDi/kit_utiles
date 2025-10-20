# Puede fallar si unique_sorted no maneja strings bien o mezcla tipos.
from kit_utiles.numbers import unique_sorted

def test_unique_sorted_strings():
    datos = ["b", "a", "a", "c"]
    assert unique_sorted(datos) == ["a", "b", "c"]
