from kit_utiles.strings import validate_email

def test_validate_email_more_extremes():
    # extremos del dominio y subdominios válidos
    assert validate_email("x@a.bz")         # TLD mínimo válido (>=2)
    assert validate_email("user@a.b.cafe")  # TLD intermedio

    # casos KO ya contemplados en tus otros tests, añadimos alguno adicional
    assert not validate_email("user@@example.com")
