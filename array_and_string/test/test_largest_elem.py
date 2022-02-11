import pytest

from array_and_string.largest_elem import largest_elem


@pytest.mark.parametrize(
    "nums, largest",
    [([3, 6, 1, 0], 1), ([1, 2, 3, 4], -1), ([1], 0)]
)
def test_largest_elem(nums, largest):
    assert largest_elem(nums) == largest
