from kit_utiles.cli import main, _format_number

def test_cli_commas_only(capsys):
    main(["prog", ", , , ,"])
    assert capsys.readouterr().out.strip() == "0"

def test_cli_mixed_invalid_tokens(capsys):
    main(["prog", "x, 2, bad, 3.0, --, -1"])
    # 2 + 3.0 - 1 = 4.0
    assert capsys.readouterr().out.strip() == "4.0"

def test_cli_empty_string_arg(capsys):
    main(["prog", "   "])
    assert capsys.readouterr().out.strip() == "0"

def test_format_number_negative_int_and_float():
    assert _format_number(-2.0) == "-2"
    assert _format_number(-2.5) == "-2.5"
