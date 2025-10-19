# Test compartido SUGERIDO para subirlo a la vez en ramas distintas:
# Cambia solo el texto del mensaje de aserción para forzar conflicto de merge.

from src.cli import main

def test_cli_csv_vacio(capsys):
    main(["prog", ""])
    out = capsys.readouterr().out.strip()
    assert out == "0"   # MENSAJE A: "Esperaba 0 para CSV vacío"
