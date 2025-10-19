"""Tests del ejercicio 9: validate_email (parametrización múltiple)"""
import pytest
from src.strings import validate_email


@pytest.mark.parametrize(
    "mail",
    [
        "user@example.com",
        "nombre.apellido@dominio-es.org",
        "u_1-2@subdominio123.net",
    ],
)
def test_validate_email_ok(mail):
    assert validate_email(mail)


@pytest.mark.parametrize(
    "mail",
    [
        "sin_arroba.com",
        "user@.com",
        "user@dominio.",
        "user@dominio.c",           # TLD 1 letra
        "user@dominio.muylargotld", # TLD > 10
        "@dominio.com",
        "user@dominio,com",
    ],
)
def test_validate_email_ko(mail):
    assert not validate_email(mail)
