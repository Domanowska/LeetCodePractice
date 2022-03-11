import pytest

from reverse_words_iii import reverse_words_iii


@pytest.mark.parametrize(
    "s, reversed_s",
    [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD")
    ]
)
def test_reverse_words_iii(s, reversed_s):
    assert reverse_words_iii(s) == reversed_s
