from typing import List


def pascals_triangle(num_rows: int) -> List[List[int]]:
    result = []
    for i in range(num_rows):
        curr_row = [1] * (i+1)
        if i >= 2:
            prev_row = result[i-1]
            for j in range(1, len(curr_row)-1):
                total = sum(prev_row[j-1:j+1])
                curr_row[j] = total
        result.append(curr_row)

    return result
