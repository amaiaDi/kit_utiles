from kit_utiles.numbers import clamp, grade, safe_divide

def test_grade_all_boundaries():
    assert grade(0) == "F"
    assert grade(59) == "F"
    assert grade(60) == "D"
    assert grade(69) == "D"
    assert grade(70) == "C"
    assert grade(79) == "C"
    assert grade(80) == "B"
    assert grade(89) == "B"
    assert grade(90) == "A"
    assert grade(100) == "A"

def test_clamp_equal_bounds_and_inside():
    # low == high => siempre ese valor
    assert clamp(5, 3, 3) == 3
    # valor ya en rango
    assert clamp(7, 0, 10) == 7

def test_safe_divide_negatives_and_floats():
    assert safe_divide(-4, 2) == -2.0
    assert safe_divide(7.5, 2.5) == 3.0
