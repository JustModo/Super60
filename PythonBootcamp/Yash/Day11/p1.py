def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
    assert (1, 2, 3) == (1, 2, 3)
    assert (1, 2, 3) == (1, 2, 3)


def test_list():
    assert 1 in [2, 3, 4]


def test_relation(a=5, b=6):
    assert a < b


def test_substring():
    assert 'fizz' in 'fizzbuzz'
