import pytest

from reverse_words import reverse_words


@pytest.mark.parametrize(
    "s, reversed_s",
    [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a")
    ]
)
def test_reverse_words(s, reversed_s):
    assert reverse_words(s) == reversed_s
