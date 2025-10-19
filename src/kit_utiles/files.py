from __future__ import annotations
from pathlib import Path
from typing import Iterable, List

def save_lines(path: str | Path, lines: Iterable[str]) -> None:
    """
    Escribe líneas en UTF-8, creando carpetas anidadas si no existen.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")

def load_lines(path: str | Path) -> List[str]:
    """
    Lee líneas en UTF-8.
    - Si el archivo NO existe => []
    - Si existe pero está vacío => []
    """
    p = Path(path)
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")
    if text == "":
        return []
    return [ln.rstrip("\n") for ln in text.splitlines()]

# Utilidades previas usadas en fases 1/2
def write_lines(path: str | Path, lines: Iterable[str]) -> None:
    save_lines(path, lines)

def read_lines(path: str | Path) -> List[str]:
    return load_lines(path)

def file_size(path: str | Path) -> int:
    p = Path(path)
    return p.stat().st_size if p.exists() else 0
