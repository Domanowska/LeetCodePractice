import pytest

from max_consecutive_ones import max_consecutive_ones


@pytest.mark.parametrize(
    "nums, con_ones",
    [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([1, 0, 0, 0, 1, 1], 2),
        ([1, 1, 1, 1, 1, 1], 6),
        ([0, 0, 0, 0, 0, 0], 0)
    ]
)
def test_max_consecutive_ones(nums, con_ones):
    assert max_consecutive_ones(nums) == con_ones
