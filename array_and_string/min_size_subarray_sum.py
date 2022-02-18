from typing import List

# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray
# [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than
# or equal to target. If there is no such subarray, return 0 instead.


# Iterative approach (n^2)
# def min_size_subarray_sum(target: int, nums: List[int]) -> int:
#     # Two pointers for beginning of subarray and end of subarray
#     start = 0
#     end = 0
#     # Keep track of total of subarray elems
#     total = nums[0]
#     # Keep track of current minimum length
#     min_len = len(nums) + 1
#
#     # Loop until we get to the end of the num array
#     while end < len(nums):
#         print("Start, end:", start, end)
#         # If total is greater than or equal to target we have found a possible subarray
#         if total >= target:
#             # See if length of subarray is the minimum length so far
#             min_len = min(min_len, len(nums[start:end+1]))
#             # We're going to shift to find the next subarray, so adjust total
#             total -= nums[start]
#             # Move to next elem in array
#             start += 1
#         # Keep going
#         else:
#             end += 1
#             if end < len(nums):
#                 total += nums[end]
#
#     # If min_len is still set to the total length of array + 1 return 0 instead
#     return 0 if min_len >= len(nums) + 1 else min_len

# Binary search (n log n)
def min_size_subarray_sum(target: int, nums: List[int]) -> int:
    # Store our result
    min_len = len(nums) + 1

    # Our target is a sum, so work with an array of sums
    sums = nums
    for n in range(1, len(nums)):
        sums[n] = sums[n-1] + nums[n]

    # Loop through the original array
    for i in range(len(nums)):
        # Two pointers pointing to the start and end of the subarray
        start = i
        end = len(nums) - 1
        print("Start:", start, "End:", end)
        # We have to adjust our target based on where the subarray starts
        # unless we're at the first iteration
        new_target = target if i == 0 else target + sums[i-1]
        print("New target:", new_target)

        # Divide and search until pointers cross
        while start <= end:
            middle = (end + start) // 2
            print("Middle:", middle, "=", sums[middle])
            # Adjust pointers based on target
            if sums[middle] < new_target:
                start = middle + 1
            else:
                end = middle - 1
            print("Adjusted start:", start, "Adjusted end:", end)

        # If we haven't gotten past the end of the array, we found our target
        if start < len(nums):
            # Check to see if we have our minimum length
            print("min_len:", min_len, "?", len(nums[i:start + 1]), "=")
            min_len = min(min_len, len(nums[i:start + 1]))
            print(min_len)

    # If min_len is still larger than our array return 0, else return the result
    return 0 if min_len >= len(nums) + 1 else min_len
