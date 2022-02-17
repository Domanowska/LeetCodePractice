from typing import List

# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray
# [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than
# or equal to target. If there is no such subarray, return 0 instead.


def min_size_subarray_sum(target: int, nums: List[int]) -> int:
    # Two pointers for beginning of subarray and end of subarray
    start = 0
    end = 0
    # Keep track of total of subarray elems
    total = nums[0]
    # Keep track of current minimum length
    min_len = len(nums) + 1

    # Loop until we get to the end of the num array
    while end < len(nums):
        print("Start, end:", start, end)
        # If total is greater than or equal to target we have found a possible subarray
        if total >= target:
            # See if length of subarray is the minimum length so far
            min_len = min(min_len, len(nums[start:end+1]))
            # We're going to shift to find the next subarray, so adjust total
            total -= nums[start]
            # Move to next elem in array
            start += 1
        # Keep going
        else:
            end += 1
            if end < len(nums):
                total += nums[end]

    # If min_len is still set to the total length of array + 1 return 0 instead
    return 0 if min_len >= len(nums) + 1 else min_len
