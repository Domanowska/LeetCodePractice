# Given an integer array nums of 2n integers,
# group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized.
# Return the maximized sum.
from typing import List


def array_partition(nums: List[int]) -> int:
    # To get an optimized max sum, and since we're taking the min,
    # we want to group numbers close together
    # Example = min(6, 6) = 6, min(6, 5) = 5
    # but min(6, 1) = 1, min(5, 2) = 2

    # Therefore, sort the array first
    sort_nums = sorted(nums)

    # Store the result
    max_sum = 0
    # Set up pointers for pairs
    first = 0
    second = 1

    while second < len(nums):
        print(sort_nums[first:second+1])
        max_sum += min(sort_nums[first:second+1])
        # Update pointers to point to next pair
        first += 2
        second += 2

    return max_sum
