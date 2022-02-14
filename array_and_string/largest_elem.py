from typing import List


def largest_elem(nums: List[int]) -> int:
    # Find largest number
    largest_index = 0
    largest = nums[0]
    for i, x in enumerate(nums):
        if x > largest:
            largest = x
            largest_index = i

    # Check if largest number is at least twice as much every other number
    for i, x in enumerate(nums):
        # If this is the largest number skip it
        if i == largest_index:
            pass
        elif 2 * x > largest:
            return -1
    # We've gotten through the loop which means the number is at least twice as
    # big as every other number
    return largest_index
