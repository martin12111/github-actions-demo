from hello import add


def test_add():
    assert 2 == add(1, 1)
    assert 4 == add(3, 1)
    assert 8 == add(3, 5)
