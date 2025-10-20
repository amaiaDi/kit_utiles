from kit_utiles.strings import word_count

def test_word_count_symbols_and_mixed():
    txt = "¿Qué? ¡Qué! -- qué; ... Árbol, árbol; árbol."
    wc = word_count(txt)
    assert wc.get("que", 0) >= 3
    assert wc.get("arbol", 0) >= 3

def test_word_count_empty_string():
    assert word_count("") == {}
