from typing import List


def spiral_matrix(mat: List[List[int]]) -> List[int]:
    result = []
    # direction starts with right, can also be; down, left, up
    direction = "right"
    row, col = 0, 0

    # Set boundaries for current loop in spiral
    top_bound = -1
    bottom_bound = len(mat)
    left_bound = -1
    right_bound = len(mat[0])

    # Loop until we've gotten all the elements
    while len(result) < len(mat) * len(mat[0]):
        print("Direction:", direction)
        print(
            "Top bound:", top_bound,
            "Bottom bound:", bottom_bound,
            "Left bound:", left_bound,
            "Right bound", right_bound
        )
        print("Current element row:", row, "- col:", col)
        # Add current element to result
        result.append(mat[row][col])

        # Find next element
        if direction == "down":
            new_row = row + 1
            new_col = col
        elif direction == "up":
            new_row = row - 1
            new_col = col
        elif direction == "right":
            new_row = row
            new_col = col + 1
        elif direction == "left":
            new_row = row
            new_col = col - 1
        else:
            print(f"Direction {direction} is not valid")
            break
        print("Next elem row:", new_row, "col:", new_col)

        # Is element out of bounds? If not we need to find next elem in spiral
        if new_row == bottom_bound:
            direction = "left"
            # We've completed a column all the way down, adjust boundary
            right_bound = col
            col -= 1
        elif new_row == top_bound:
            direction = "right"
            # We've completed a whole column up, adjust boundary
            left_bound = col
            col += 1
        elif new_col == right_bound:
            direction = "down"
            # We've completed a whole top row, adjust boundary
            top_bound = row
            row += 1
        elif new_col == left_bound:
            direction = "up"
            # We've completed a whole row over, adjust boundary
            bottom_bound = row
            row -= 1
        else:
            row = new_row
            col = new_col
        print("Actual elem row:", row, "col:", col)
    return result
