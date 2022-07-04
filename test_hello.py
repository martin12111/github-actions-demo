from hello import add


def test_add():
    assert 2 == add(1, 1)
    assert 4 == add(3, 1)
    assert 8 == add(3, 5)
    
def test_add_2():
    assert 1 == add(0, 1)
    assert 3 == add(2, 1)
    assert 7 == add(2, 5)
