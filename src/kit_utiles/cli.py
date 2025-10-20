from __future__ import annotations
import sys

def _format_number(x: float) -> str:
    """Imprime sin .0 si es entero exacto."""
    if x == int(x):
        return str(int(x))
    return str(x)

def main(argv: list[str] | None = None) -> int:
    """
    Espera una línea CSV como último argumento.
    - Si CSV vacío/espacios → imprime "0"
    - Suma números y siempre imprime como float (p.ej. "6.0")
    """
    if argv is None:
        argv = sys.argv[1:]

    csv = ""
    if len(argv) >= 1:
        # en tests: ["prog", "1,2,3"] → último argumento es el CSV
        csv = argv[-1].strip()

    tokens = [t.strip() for t in csv.split(",")] if csv else []
    tokens = [t for t in tokens if t]  # descarta vacíos

    if not tokens:
        print("0")
        return 0

    total = 0.0
    for t in tokens:
        try:
            total += float(t)
        except ValueError:
            # ignora tokens no numéricos
            continue

    # siempre como float (ej: 6.0)
    print(f"{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
