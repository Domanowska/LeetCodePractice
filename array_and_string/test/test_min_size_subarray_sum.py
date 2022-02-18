import pytest

from min_size_subarray_sum import min_size_subarray_sum


@pytest.mark.parametrize(
    "target, nums, length",
    [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 2, 4], 1),
        (4, [4, 2, 1], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (11, [1, 2, 3, 4, 5], 3)
    ]
)
def test_min_size_subarray_sum(target, nums, length):
    assert min_size_subarray_sum(target, nums) == length
