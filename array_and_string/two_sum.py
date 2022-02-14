# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
# order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2
#
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
# Your solution must use only constant extra space.
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # Pointers for the two indexes
    i_1 = 0
    i_2 = len(nums) - 1

    while i_1 < i_2:
        total = nums[i_1] + nums[i_2]
        if total == target:
            return [i_1 + 1, i_2 + 1]
        elif total < target:
            i_1 += 1
        elif total > target:
            i_2 -= 1

    # We got here and no solution was returned
    return [-1, -1]
