from kit_utiles.files import file_size, write_lines, read_lines
from pathlib import Path

def test_file_size_no_existe(tmp_path):
    p = tmp_path / "missing.txt"
    assert file_size(p) == 0

def test_alias_write_read(tmp_path):
    p = tmp_path / "datos.txt"
    write_lines(p, ["uno", "dos"])
    assert read_lines(p) == ["uno", "dos"]
