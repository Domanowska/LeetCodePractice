from typing import List


def increment_digits(digits: List[int]) -> List[int]:
    # reversed_digits = list(reversed(digits))     # O(n)
    # for i, x in enumerate(reversed_digits):     # O(n)
    #     print(i, x)
    #     if x == 9:
    #         reversed_digits[i] = 0
    #         if i == len(digits) - 1:
    #             reversed_digits.append(1)
    #             break
    #     else:
    #         reversed_digits[i] += 1
    #         break
    # return list(reversed(reversed_digits))  # O(n)

    # move along the input array starting from the end
    n = len(digits)
    for i in range(n):    # O(n)
        idx = n - 1 - i
        # set all the nines at the end of array to zeros
        if digits[idx] == 9:
            digits[idx] = 0
        # here we have the rightmost not-nine
        else:
            # increase this rightmost not-nine by 1
            digits[idx] += 1
            # job is done
            return digits
    # We've gone through the whole loop and not returned because they're all 9's
    return [1] + digits
