from my_math import add


def test_two_numbers():
    assert add(1, 2) == 3


def test_two_strings():
    assert add("hello", "world") == "helloworld"


def test_negative_numbers():
    assert add(-1, -2) == -3
