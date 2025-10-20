from pathlib import Path
from kit_utiles.files import save_lines, load_lines, file_size

def test_save_empty_creates_file(tmp_path: Path):
    p = tmp_path / "sub" / "empty.txt"
    save_lines(p, [])
    # El archivo debe existir aunque esté vacío
    assert p.exists()
    assert file_size(p) == 0
    assert load_lines(p) == []
