from kit_utiles.strings import (
    normalize_whitespace, is_palindrome, snake_to_camel, validate_email
)

def test_normalize_whitespace_tabs_and_spaces():
    assert normalize_whitespace("\t  hola\t \n  mundo  ") == "hola mundo"

def test_is_palindrome_spaces_cases():
    assert is_palindrome("Anita   lava   la  Tina")
    assert not is_palindrome("No lo es")

def test_snake_to_camel_underscores_corner():
    # múltiples guiones bajos, al principio/fin
    assert snake_to_camel("__many___underscores__") == "ManyUnderscores"
    # solo guiones bajos -> cadena vacía
    assert snake_to_camel("__") == ""

def test_validate_email_with_hyphens_inside_and_long_tld():
    # guiones en medio del label (válido)
    assert validate_email("a-b.c_d@sub-domain.example.org")
