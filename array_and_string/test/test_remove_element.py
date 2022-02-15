import pytest

from remove_element import remove_element


@pytest.mark.parametrize(
    "nums, val, length, expected_nums",
    [
        ([3, 2, 2, 3], 3, 2, [2, 2, 3, 3]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5,  [0, 1, 4, 0, 3, 2, 2, 2]),
        ([2], 3, 1, [2]),
        ([1], 1, 0, [])
    ]
)
class TestRemoveElement:
    def test_remove_element_returns_correct_length(
            self, nums, val, length, expected_nums
    ):
        assert remove_element(nums, val) == length

    def test_remove_element_has_updated_nums_correctly(
            self, nums, val, length, expected_nums
    ):
        remove_element(nums, val)
        assert set(nums[:length]) == set(expected_nums[:length])
