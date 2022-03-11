def reverse_words_iii(s):
    result = []
    i = j = 0
    while i < len(s):
        # Have we reached the end of the string, or have we reached the end of a word?
        if j >= len(s) or s[j] == " ":
            this_word = ""
            # The next word is after the space
            next_word = j + 1
            # Go  back to the last letter
            j -= 1
            # Add letters to the result until the beginning of the word
            while j >= i:
                this_word += s[j]
                j -= 1
            # Add the word to the result
            result.append(this_word)
            # Move on to the next word
            i = j = next_word
        # We need to keep going until we find a complete word
        j += 1

    return " ".join(result)
