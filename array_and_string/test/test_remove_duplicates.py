import pytest

from remove_duplicates import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected_nums",
    [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([1, 2], [1, 2]),
        ([1, 1], [1])
    ]
)
def test_remove_duplicates(nums, expected_nums):
    k = remove_duplicates(nums)
    assert k == len(expected_nums)
    assert nums[:k] == expected_nums
