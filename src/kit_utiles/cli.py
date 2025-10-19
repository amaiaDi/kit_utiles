from __future__ import annotations
import sys

def _format_number(x: float) -> str:
    """Imprime sin .0 si es entero exacto."""
    if x == int(x):
        return str(int(x))
    return str(x)

def main(argv: list[str] | None = None) -> int:
    """
    CLI muy simple que espera una cadena CSV con números (ints/floats).
    - Si el CSV está vacío o contiene solo espacios/comas => imprime "0".
    - Si hay valores, suma y lo imprime (sin .0 si es entero).
    Casos pensados para tests E17/E18.
    """
    if argv is None:
        argv = sys.argv[1:]

    csv = argv[0] if argv else ""
    tokens = [t.strip() for t in csv.split(",")] if csv else []
    tokens = [t for t in tokens if t]  # descartar vacíos

    if not tokens:
        print("0")
        return 0

    total = 0.0
    for t in tokens:
        try:
            total += float(t)
        except ValueError:
            # Si aparece un token no numérico, lo ignoramos de forma segura.
            # (Ajustable según tests: si hubiera que lanzar error, cambiar aquí)
            continue

    print(_format_number(total))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
