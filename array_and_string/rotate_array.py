from typing import List


def rotate_array(nums: List[int], k: int) -> None:
    if k == 0 or k % len(nums) == 0:
        return

    # A variable to keep track of where we started, to catch loops
    start = 0
    # Which index are we on now
    curr = 0
    # Hold the variable in the current index
    tmp = nums[curr]

    print("\nstart:", start, curr, tmp)
    for i in range(len(nums)):
        # Find which index we want to shift this variable to
        shift_to = (curr + k) % len(nums)
        print("Shift to:", shift_to)
        # Write current elem to that index, hold the elem at that index
        nums[shift_to], tmp = tmp, nums[shift_to]
        print("tmp:", tmp)
        # Move to the index we just shifted to
        curr = shift_to
        # If we've hit a loop go to the next index
        if curr == start:
            curr += 1
            # Keep track of new tmp
            tmp = nums[curr]
            # Keep track of new start
            start += 1

        print("Next index:", curr)
        print(nums)
        print("----------")


#  Below solution does not use O(1) space
# def rotate_array(nums: List[int], k: int) -> None:
#     k %= len(nums)
#     pivot = -k
#     nums[:] = nums[pivot:] + nums[:pivot]
