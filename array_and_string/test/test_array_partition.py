import pytest

from array_partition import array_partition


@pytest.mark.parametrize("nums, max_sum", [([1, 4, 3, 2], 4), ([6, 2, 6, 5, 1, 2], 9)])
def test_array_partition(nums, max_sum):
    assert array_partition(nums) == max_sum
