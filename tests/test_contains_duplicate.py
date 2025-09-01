from problems.contains_duplicate import has_duplicate, has_duplicate_v2

def test_has_duplicate():
    assert has_duplicate([1, 2, 3, 1]) is True
    assert has_duplicate([1, 2, 3, 4]) is False

def test_has_duplicate_v2():
    assert has_duplicate_v2([1, 2, 3, 1]) is True
    assert has_duplicate_v2([1, 2, 3, 4]) is False