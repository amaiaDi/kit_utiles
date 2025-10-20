from kit_utiles.cli import main, _format_number
import sys

def test_cli_sin_argumentos(capsys):
    main(["prog"])
    assert capsys.readouterr().out.strip() == "0"

def test_cli_mixto_y_negativos(capsys):
    main(["prog", " 1, x, -2.5 , 3 "])
    # 1 - 2.5 + 3 = 1.5
    assert capsys.readouterr().out.strip() == "1.5"

def test_cli_float_y_entero(capsys):
    main(["prog", "5.0,5"])
    # 10.0 -> se imprime como float
    assert capsys.readouterr().out.strip() == "10.0"

def test_format_number_interno():
    assert _format_number(7.0) == "7"
    assert _format_number(7.5) == "7.5"
