# Si load_lines no devuelve [], falla el caso de archivo vacío.
# Si save_lines no crea carpetas, fallará el nested.
from pathlib import Path
from src.files import save_lines, load_lines

def test_load_lines_empty(tmp_path: Path):
    p = tmp_path / "vacio.txt"
    p.write_text("", encoding="utf-8")
    assert load_lines(p) == []

def test_roundtrip_nested(tmp_path: Path):
    p = tmp_path / "a" / "b" / "out.txt"
    save_lines(p, ["x","y"])
    assert load_lines(p) == ["x","y"]
