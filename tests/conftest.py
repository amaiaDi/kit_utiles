from __future__ import annotations
import sys
from typing import Callable, List, Iterable
import builtins
import io
from contextlib import redirect_stdout

import pytest

# --- FIXTURE: raíz de paquete ya visible gracias a pythonpath=["src"] en pyproject ---
# Si no tuvieras ese ajuste, podrías añadir dinámicamente src al sys.path aquí.

@pytest.fixture
def run_cli_capture() -> Callable[[List[str]], str]:
    """
    Ejecuta kit_utiles.cli.main(argv) y devuelve stdout (stripeado).
    Útil para E17/E18: CSV vacío, espacios, etc.
    """
    from kit_utiles.cli import main

    def _run(args: List[str]) -> str:
        buf = io.StringIO()
        # redirigimos stdout para capturar lo que imprime main()
        with redirect_stdout(buf):
            main(args)
        return buf.getvalue().strip()

    return _run


@pytest.fixture
def tmp_lines_file(tmp_path):
    """
    Crea un archivo temporal con algunas líneas y devuelve su ruta.
    Útil para tests de files.load_lines/save_lines.
    """
    p = tmp_path / "nested" / "sample.txt"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("uno\ndos\ntres\n", encoding="utf-8")
    return p


@pytest.fixture
def make_lines(tmp_path) -> Callable[[Iterable[str], str], str]:
    """
    Genera rápidamente un archivo con líneas dadas; devuelve la ruta.
    """
    def _make(lines: Iterable[str], name: str = "data.txt") -> str:
        p = tmp_path / name
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return str(p)
    return _make


@pytest.fixture
def patch_input(monkeypatch) -> Callable[[str], None]:
    """
    Parchea input() si algún test lo requiere.
    """
    def _patch(value: str) -> None:
        it = iter([value])
        monkeypatch.setattr(builtins, "input", lambda: next(it))
    return _patch
