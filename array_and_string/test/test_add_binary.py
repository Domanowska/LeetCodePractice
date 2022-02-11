import pytest

from array_and_string.add_binary import add_binary


@pytest.mark.parametrize(
    "a, b, sum_ab",
    [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1111", "1111", "11110"),
        ("0", "11", "11")
    ]
)
def test_add_binary(a, b, sum_ab):
    assert add_binary(a, b) == sum_ab
