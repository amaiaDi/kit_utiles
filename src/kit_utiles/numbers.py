from __future__ import annotations
from typing import Iterable, Union, List

Number = Union[int, float]

# ---------- Utilidades "clásicas" ----------
def clamp(x: Number, low: Number, high: Number) -> Number:
    """Restringe x al rango [low, high]."""
    if low > high:
        raise ValueError("low cannot be greater than high")
    return max(low, min(high, x))

def mean(values: Iterable[Number]) -> float:
    """Media aritmética; ValueError si secuencia vacía."""
    vals: List[Number] = list(values)
    if not vals:
        raise ValueError("values cannot be empty")
    return float(sum(vals)) / len(vals)

# ---------- Requeridos por E11, E12, E13, E16, E20 ----------
def sum_list(values: Iterable[Number]) -> float:
    """Suma robusta de ints/floats (soporta negativos)."""
    total = 0.0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("sum_list only accepts int or float values")
        total += v
    return float(total)

def unique_sorted(values: Iterable[str]) -> list[str]:
    """
    Devuelve lista sin duplicados y ordenada.
    Según el test, se usará con cadenas.
    """
    return sorted(set(values))

def safe_divide(a: Number, b: Number) -> float:
    """
    Divide a/b validando tipos numéricos.
    Lanza TypeError si a o b no son int/float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("safe_divide requires numeric types (int/float)")
    if b == 0:
        return float("inf")  # o podría ser raise/0; el test E13 valida tipos
    return float(a) / float(b)

def grade(value: int) -> str:
    """
    Nota en letras para enteros 0..100:
      A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
    - TypeError si no es int
    - ValueError si fuera de rango
    """
    if not isinstance(value, int):
        raise TypeError("grade requires an integer 0..100")
    if not (0 <= value <= 100):
        raise ValueError("grade must be in range 0..100")
    if value >= 90: return "A"
    if value >= 80: return "B"
    if value >= 70: return "C"
    if value >= 60: return "D"
    return "F"
