"""Tests del ejercicio 8: CLI (captura de salida con capsys)"""
from kit_utiles.cli import main


def test_main_suma_basica(capsys):
    main(["prog", "1,2,3"])
    out = capsys.readouterr().out.strip()
    assert out == "6.0"


def test_main_sin_argumentos(capsys):
    main(["prog"])
    out = capsys.readouterr().out.strip()
    assert out == "0"
