from __future__ import annotations
import re
import unicodedata
from collections import Counter
from typing import Dict, Iterable

# ---------- Utilidades "clásicas" usadas en Fase 1/2 ----------
def normalize_whitespace(text: str) -> str:
    """Colapsa espacios múltiples y recorta extremos."""
    return " ".join(text.split())

def is_palindrome(text: str, ignore_case: bool = True) -> bool:
    """Comprueba si un texto es palíndromo (ignorando espacios)."""
    t = "".join(ch for ch in text if not ch.isspace())
    if ignore_case:
        t = t.lower()
    return t == t[::-1]

def join_chars(items: Iterable[object]) -> str:
    """Une elementos convirtiéndolos en str (seguro para tipos no str)."""
    return "".join(map(str, items))

def snake_to_camel(name: str) -> str:
    """snake_case -> CamelCase (múltiples guiones bajos tolerados)."""
    return "".join(part.capitalize() for part in name.split("_") if part)

# ---------- Funciones requeridas por tests E14, E19 ----------
_PUNCT_RE = re.compile(r"[^\w\s]", flags=re.UNICODE)

def _strip_accents(s: str) -> str:
    """Quita tildes/acentos normalizando a NFKD y filtrando marcas."""
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if unicodedata.category(ch) != "Mn")

def word_count(text: str) -> Dict[str, int]:
    """
    Cuenta palabras normalizando:
      - minúsculas
      - sin tildes
      - sin puntuación
    """
    if not text:
        return {}
    # 1) bajar a minúsculas
    t = text.lower()
    # 2) eliminar acentos/diacríticos (qué→que, árbol→arbol, ñ→n)
    t = _strip_accents(t)
    # 3) quitar signos y separar por no alfanumérico
    #    (¿?¡!.,;:… comillas, paréntesis, etc.)
    t = re.sub(r"[^a-z0-9]+", " ", t)

    t = _PUNCT_RE.sub(" ", t)
    tokens = t.split()
    return dict(Counter(tokens))

# Acepta subdominios y TLD 2–10 letras; usuario con ._%+-
_EMAIL_RE = re.compile( r'^[A-Za-z0-9._-]+@'     # usuario
    r'(?:[A-Za-z0-9-]+\.)+'  # >=1 subdominio
    r'[A-Za-z]{2,10}$'       # TLD 2..10)
)

def validate_email(email: str) -> bool:
    """Valida emails con subdominios y TLD de 2 a 9 letras."""
    return bool(_EMAIL_RE.match(email or ""))
