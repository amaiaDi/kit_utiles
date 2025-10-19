# Este test puede fallar si sum_list no soporta floats/negativos correctamente.
# Si falla, revisa el tipo de acumulador (empieza en 0 y suma tal cual).
from src.numbers import sum_list

def test_sum_list_negativos_y_floats():
    assert sum_list([-2, 0.5, 1.5]) == 0.0
