"""Tests del ejercicio 6: save_lines / load_lines (tmp_path)"""
from pathlib import Path
from kit_utiles.files import save_lines, load_lines


def test_roundtrip_tmp_path(tmp_path: Path):
    destino = tmp_path / "salida.txt"
    data = ["uno", "dos", "tres"]
    save_lines(destino, data)
    leido = load_lines(destino)
    assert leido == data


def test_load_lines_vacio(tmp_path: Path):
    destino = tmp_path / "vacio.txt"
    destino.write_text("", encoding="utf-8")
    assert load_lines(destino) == []
