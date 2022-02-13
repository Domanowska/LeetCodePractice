def reversed_string(input_string):
    # Pointers to keep track of which chars we're swapping
    start = 0
    end = len(input_string) - 1

    # Loop until we meet in the middle of string
    while start < end:
        # Swap chars
        input_string[start], input_string[end] = input_string[end], input_string[start]
        # Update pointers
        start += 1
        end -= 1
