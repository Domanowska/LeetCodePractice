import pytest

from two_sum import two_sum


@pytest.mark.parametrize(
    "nums, target, indexes",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3], 6, [-1, -1])
    ]
)
def test_two_sum(nums, target, indexes):
    assert two_sum(nums, target) == indexes
