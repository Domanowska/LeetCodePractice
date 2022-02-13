def longest_common_prefix(strs):
    # Easiest answer: smallest word is in all other words and we're done!
    prefix = min(strs, key=len)     # built in function = O(n)
    prefix_length = len(prefix)
    print("Prefix:", prefix)
    for i in range(len(strs)):      # O(n)
        this_word = strs[i]
        print("Word:", this_word)
        if this_word[:prefix_length] != prefix:
            # Decrease the prefix and see if it matches
            while prefix:       # O(m) where m is the number of letters left in prefix
                prefix = prefix[:prefix_length - 1]
                prefix_length = len(prefix)
                print("Try prefix:", prefix)
                if this_word[:prefix_length] == prefix:
                    break
    return prefix
