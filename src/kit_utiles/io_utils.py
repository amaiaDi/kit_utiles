from pathlib import Path
from typing import Iterable

def write_lines(path: str | Path, lines: Iterable[str]) -> None:
    """Escribe líneas en UTF-8, creando carpetas si faltan."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")

def read_lines(path: str | Path) -> list[str]:
    p = Path(path)
    if not p.exists():
        return []
    with p.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def file_size(path: str | Path) -> int:
    p = Path(path)
    return p.stat().st_size if p.exists() else 0
