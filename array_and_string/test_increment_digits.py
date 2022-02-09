import pytest

from increment_digits import increment_digits


@pytest.mark.parametrize(
    "digits, digits_inc",
    [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([1, 9, 9, 9], [2, 0, 0, 0]),
        ([9, 9, 9, 9], [1, 0, 0, 0, 0])
    ]
)
def test_increment_digits(digits, digits_inc):
    assert increment_digits(digits) == digits_inc
