# Returns pointer to the first occurrence of needle in haystack
# See: http://www.cplusplus.com/reference/cstring/strstr/
def strStr(haystack: str, needle: str) -> int:
    # If needle is empty return 0
    if not needle:
        return 0

    # Loop through haystack until needle is found
    for i in range(len(haystack)):
        # See if next few chars match all of needle
        if haystack[i:i+len(needle)] == needle:
            return i

    # We have gotten here and nothing was found
    return -1
