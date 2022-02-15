from typing import List

# Given an integer array nums and an integer val, remove all occurrences of val in nums
# in-place. The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.


def remove_element(nums: List[int], val: int) -> int:
    # Set up two pointers to keep track of the beginning and end of nums
    i = 0

    print("Original nums:", nums)
    # Loop until pointers meet
    while i < len(nums):
        # if nums[i] is the value we're looking to remove,
        # we need to swap it with a different value from the back of the array
        if nums[i] == val:
            end = len(nums) - 1
            nums[i], nums[end] = nums[end], nums[i]
            print("Swapped", nums[i], nums[end])
            # Remove the last element
            nums.pop()
            print("New nums:", nums)
        # Otherwise increment front pointer
        else:
            i += 1

    print("Final nums:", nums)
    return len(nums)
