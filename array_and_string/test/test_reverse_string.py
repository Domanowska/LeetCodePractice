import pytest

from reverse_string import reversed_string


@pytest.mark.parametrize(
    "input_string, rev_string",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
    ]
)
def test_reverse_string(input_string, rev_string):
    reversed_string(input_string)
    assert input_string == rev_string
