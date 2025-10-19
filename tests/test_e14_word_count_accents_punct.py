# Este test comprueba normalización de acentos y limpieza de signos.
# Si falla, ajusta strings._strip_accents (NFD + quitar Mn) y regex para dejar sólo letras/espacios.
from src.strings import word_count

def test_word_count_acentos_y_signos():
    texto = "¿Qué, qué? ¡Árbol! árbol... ÁrBoL"
    wc = word_count(texto)
    # Tras normalizar y a minúsculas, "qué" -> "que", "árbol" -> "arbol"
    assert wc.get("que", 0) == 2
    assert wc.get("arbol", 0) == 3
