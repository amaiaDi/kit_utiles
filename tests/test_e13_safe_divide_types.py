# Si safe_divide no valida tipos, este test debe fallar:
# Arreglo sugerido: comprobar isinstance(a,(int,float)) e idem b, y lanzar TypeError con mensaje claro.
import pytest
from kit_utiles.numbers import safe_divide

def test_safe_divide_tipo_invalido():
    with pytest.raises(TypeError):
        safe_divide("4", 2)
