# Given an m x n matrix mat, return an array of all the elements of the array in a
# diagonal order.
#
# def diagonal_traverse(mat):
#     result = []
#     # Keep track of beginning elem
#     m = n = 0
#     # Diagonals are at the top and right, loop through them
#     how_many_diags = len(mat) + len(mat[0]) - 1
#     for x in range(how_many_diags):
#         # Keep track of diagonal elems
#         diagonal = []
#         # Different pointers for diag elems
#         diag_m, diag_n = m, n
#         # Loop through elems in diag
#         while diag_m < len(mat) and diag_n >= 0:
#             diagonal.append(mat[diag_m][diag_n])
#             diag_m += 1
#             diag_n -= 1
#
#         # if we're on an even numbered diagonal, reverse it before adding it to result
#         if x % 2 == 0:
#             diagonal = list(reversed(diagonal))
#         result += diagonal
#
#         # Find the next diagonal
#         if n < len(mat[0]) - 1:
#             n += 1
#         else:
#             n = len(mat[0]) - 1     # Just in case n is out of bounds now
#             m += 1
#
#     return result


# ATTEMPT 1
def diagonal_traverse(mat):
    # Store resulting array
    diagonal = []
    # Starting element
    row = col = 0
    # Starting direction - Going up == True
    direction = True

    # loop until we reach the bottom right corner of 2d array
    while row < len(mat) and col < len(mat[0]):
        print("Current elem:", mat[row][col], "Row:", row, "Col:", col)
        # Add element to result
        diagonal.append(mat[row][col])
        print("Result:", diagonal)

        print("Going up?", direction)
        # Find next elem
        if direction:
            new_row = row - 1
            new_col = col + 1
        else:
            new_row = row + 1
            new_col = col - 1
        print("Next elem:", "Row:", new_row, "Col:", new_col)

        # Is this next elem out of bounds of the matrix?
        if new_row < 0 or new_row >= len(mat) or new_col < 0 or new_col >= len(mat[0]):
            if direction:
                # Have we reached the right hand side?
                if col >= len(mat[0]) - 1:
                    row += 1
                # There are still more columns to go
                if col < len(mat[0]) - 1:
                    col += 1
                # Flip direction
                direction = False
                # We're at the top
            else:
                # We're at the bottom?
                if row >= len(mat) - 1:
                    col += 1
                # There are more rows to go
                if row < len(mat) - 1:
                    row += 1
                # Flip direction
                direction = True
            print("Adjusted Current elem:", "Row:", row, "Col:", col)
        else:
            # In bounds just make next elem curr elem
            row, col = new_row, new_col
    return diagonal
