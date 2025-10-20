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
        argv = sys.argv

    # En tests nos pasan ["prog", "1,2,3"] o ["prog"]
    csv = argv[1].strip() if len(argv) >= 2 else ""

    tokens = [t.strip() for t in csv.split(",")] if csv else []
    tokens = [t for t in tokens if t]  # descarta vacíos

    if not tokens:
        print("0")          # ← EXACTO: "0" (no "0.0")
        return 0

    total = 0.0
    for t in tokens:
        try:
            total += float(t)
        except ValueError:
            continue  # ignora tokens no numéricos

    print(f"{total}")       # siempre float (p.ej. 6.0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
