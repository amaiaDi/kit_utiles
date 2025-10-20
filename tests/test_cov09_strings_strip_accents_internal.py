# Cubrimos la función interna para asegurar líneas de normalización
from kit_utiles.strings import _strip_accents

def test__strip_accents_varios():
    assert _strip_accents("áéíóúüñÁÉÍÓÚÜÑ") == "aeiouunAEIOUUN"
    assert _strip_accents("canción árbol pingüino") == "cancion arbol pinguino"
