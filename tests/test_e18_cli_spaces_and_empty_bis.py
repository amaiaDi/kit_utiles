# Versión alternativa del test compartido con un comentario distinto para provocar conflicto.

from src.cli import main

def test_cli_csv_vacio_bis(capsys):
    main(["prog", "  ,  ,  "])
    out = capsys.readouterr().out.strip()
    assert out == "0"   # MENSAJE B: "CSV con espacios también debe dar 0"
