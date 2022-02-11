import pytest

from strStr import strStr


@pytest.mark.parametrize(
    "haystack, needle, pointer", [("hello", "ll", 2), ("aaaaa", "bba", -1), ("", "", 0)]
)
def test_strStr(haystack, needle, pointer):
    assert strStr(haystack, needle) == pointer
