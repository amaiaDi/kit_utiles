from kit_utiles.numbers import sum_list

def test_sum_list_large_sequence():
    vals = [0.1] * 100 + [1, -1, 2.5, -2.5]
    # 100*0.1 = 10.0; +1-1+2.5-2.5 = 0 => total 10.0
    assert abs(sum_list(vals) - 10.0) < 1e-9
