def pascals_triangle_ii(index):
    result = [1] * (index + 1)

    if index >= 2:
        i, j = 1, len(result) - 2
        result[i], result[j] = index, index
        i += 1
        j -= 1
        while i <= j:
            next_val = (result[i-1] * (index - i + 1) ) // i
            result[i], result[j] = next_val, next_val
            i += 1
            j -= 1
    return result
