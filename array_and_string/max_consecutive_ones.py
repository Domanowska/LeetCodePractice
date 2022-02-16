from typing import List


def max_consecutive_ones(nums: List[int]) -> int:
    curr_max = 0
    # Pointer to keep track of beginning of window
    i = 0
    # Pointer to keep track of end of window
    j = 0

    while j < len(nums):
        if nums[j] != 1:
            curr_max = max(curr_max, j - i)
            # We're starting a new window
            i = j + 1
        j += 1

    return max(curr_max, j - i)
