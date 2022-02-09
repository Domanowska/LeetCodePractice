# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left
# of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there
# are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1
# Link: https://leetcode.com/problems/find-the-middle-index-in-array/

from typing import List


def pivot_index(nums: List[int]) -> int:
    # Not very efficient solution, O(n^2) or O(n) * O(2n)
    #
    # for i in range(len(nums)):
    #     print(sum(nums[:i]), sum(nums[i+1:]))
    #     if sum(nums[:i]) == sum(nums[i+1:]):
    #         return i
    # return -1

    right_sum = sum(nums)   # sum = O(n)
    left_sum = 0
    for i in range(len(nums)):  # O(n)  # Could also do enumerate()
        if left_sum == right_sum - nums[i] - left_sum:
            return i
        left_sum += nums[i]
    return -1
