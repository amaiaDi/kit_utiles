from kit_utiles.strings import normalize_whitespace, is_palindrome, snake_to_camel, validate_email

def test_normalize_whitespace_basico():
    assert normalize_whitespace("  Hola   mundo \n  ") == "Hola mundo"

def test_palindrome_con_espacios_y_mayusculas():
    assert is_palindrome("Anita lava la Tina")
    assert not is_palindrome("Python")

def test_snake_to_camel_bordes():
    assert snake_to_camel("_inicio") == "Inicio"
    assert snake_to_camel("final_") == "Final"
    assert snake_to_camel("doble__sub") == "DobleSub"

def test_validate_email_tld_extremos():
    # TLD de 1 o >10 letras deberían fallar
    assert not validate_email("user@mail.example.c")
    assert not validate_email("user@mail.example.toolongtld")
    # OK en rango válido
    assert validate_email("user@mail.example.com")
