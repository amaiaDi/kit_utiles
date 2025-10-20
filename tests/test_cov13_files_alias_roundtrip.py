from kit_utiles.files import write_lines, read_lines
from pathlib import Path

def test_write_read_alias_roundtrip(tmp_path: Path):
    p = tmp_path / "round" / "trip.txt"
    write_lines(p, ["uno", "dos", "tres"])
    assert read_lines(p) == ["uno", "dos", "tres"]
