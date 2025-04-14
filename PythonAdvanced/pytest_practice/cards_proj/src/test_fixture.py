import pytest
from cards import CardsDB
from pathlib import Path
from tempfile import TemporaryDirectory


@pytest.fixture
def cards_db():
    with TemporaryDirectory() as db_path:
        db_path = Path(db_path)
        cards_db = CardsDB(db_path)
        yield cards_db
        cards_db.close()


def test_empty(cards_db):
    print(cards_db.count())
    assert cards_db.count() == 0


@pytest.fixture
def hello():
    return "hello"


def test_hello(hello):
    assert hello == "hello"


@pytest.fixture
def num_list():
    return [1, 2, 3]


def test_num_list(num_list):
    assert sum(num_list) == 6


@pytest.fixture
def user_dict():
    return {"name": "Alice", "age": 30}


def test_user_dict(user_dict):
    assert user_dict["age"] == 30


@pytest.fixture
def num():
    return 5


@pytest.fixture
def num_square(num):
    return num**2


def test_num_square(num_square):
    assert num_square == 25


@pytest.fixture
def yeild_list():
    num_list = []
    yield num_list
    num_list.clear()
    

