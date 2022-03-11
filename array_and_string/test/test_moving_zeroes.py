import pytest

from moving_zeroes import moving_zeroes

@pytest.mark.parametrize(
    "nums, expected_nums",
    [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0]), ([1, 2, 3, 0], [1, 2, 3, 0])]
)
def test_moving_zeroes(nums, expected_nums):
    moving_zeroes(nums)
    assert nums == expected_nums
