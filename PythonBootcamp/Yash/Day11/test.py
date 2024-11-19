from cards import Card


def test_field_access():
    c = Card("something", "brain", "todo", 123)
    assert c.summary == "something"
    assert c.owner == "brain"
    assert c.state == "todo"
    assert c.id == 123


def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_inequality():
    cl = Card("something", "brain", "todo", 123)
    c2 = Card("completely different", "okken", "done", 123)
    assert cl != c2


def test_from_dict():
    cl = Card("something", "brain", "todo", 123)
    c2_dict = {"summary": "something",
               "owner": "brain", "state": "todo", "id": 123}
    c2 = Card.from_dict(c2_dict)
    assert cl == c2


def test_to_dict():
    cl = Card("something", "brain", "todo", 123)
    c2 = cl.to_dict()
    c2_expected = {"summary": "something",
                   "owner": "brain", "state": "todo", "id": 123}
    assert c2 == c2_expected

