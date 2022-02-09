import pytest

from pivot import pivot_index


@pytest.mark.parametrize(
    "nums, pivot",
    [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0), ([-1, 1, 2], 2)]
)
def test_pivot_index(nums, pivot):
    assert pivot_index(nums) == pivot
