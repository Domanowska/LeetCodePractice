def add_binary(a: str, b: str) -> str:
    result = []

    # Make sure strings are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    if len(a) > (len(b)):
        diff = len(a) - len(b)
        b = "0" * diff + b
    print(a, b)

    # Now we add starting from the end
    # We need a variable to remember what's carried over
    carry = 0
    for i in range(len(a)-1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        print(int(a[i]), "+", int(b[i]), "+", carry, "=", total)
        if total == 3:
            result.append('1')
            carry = 1
            print("=", result, "carry the", carry)
        elif total == 2:
            result.append('0')
            carry = 1
            print("=", result, "carry the", carry)
        else:
            result.append(str(total))
            carry = 0
            print("=", result, "carry the", carry)
    # Append the last carry if still left
    if carry == 1:
        result.append(str(carry))
    result.reverse()
    print("Final result =", result)

    return "".join(result)
