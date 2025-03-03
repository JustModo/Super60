from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field


@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=True)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)

    def to_dict(self):
        return asdict(self)


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

# 1. Modify default values in the Card Definition,
# for ex: replace some None values with an empty string or a filled-in string
# Do the tests catch?

# 2. What happens if we change compare—False to compare=True?

# 3. Are there any missing tests? Any functionality not covered?
# Add some test functions if there is something missing

# 4. Try the -k option to select a test.
