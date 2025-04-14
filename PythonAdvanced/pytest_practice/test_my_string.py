from my_string import to_uppercase


def test_string():
    assert to_uppercase("hello") == "HELLO"


def test_alphanumeric():
    assert to_uppercase("h2ello") == "H2ELLO"


def test_symbol():
    assert to_uppercase("@#$") == "@#$"


def test_number():
    assert to_uppercase(5) == 5
