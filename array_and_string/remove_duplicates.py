from typing import List


def remove_duplicates(nums: List[int]) -> int:
    curr_val, next_val = 0, 1

    while next_val < len(nums):
        # If current and next value are different
        if nums[curr_val] != nums[next_val]:
            # If current and next value are not next to each other, swap em
            if next_val - curr_val > 1:
                nums[curr_val+1] = nums[next_val]
            curr_val += 1
        next_val += 1

    return curr_val + 1
