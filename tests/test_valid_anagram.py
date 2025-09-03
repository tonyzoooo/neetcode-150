import pytest

from problems.valid_anagram import is_anagram, is_anagram_v2

@pytest.mark.parametrize("s, t, expected", [
    ("listen", "silent", True),
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("", "", True),
    ("ab", "a", False),
    ("aabbcc", "abcabc", True),
    ("aabbcc", "abccba", True),
    ("aabbcc", "aabbc", False)
])
def test_is_anagram(s, t, expected):
    assert is_anagram(s, t) == expected
    assert is_anagram_v2(s, t) == expected