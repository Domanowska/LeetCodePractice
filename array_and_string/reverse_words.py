def reverse_words(s):
    s_array = s.split()

    i, j = 0, len(s_array) - 1

    while i < j:
        s_array[i], s_array[j] = s_array[j], s_array[i]
        i += 1
        j -= 1

    return " ".join(s_array)

