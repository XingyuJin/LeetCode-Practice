"""
@Description
Converts fist string to an integer or 0 otherwise.

@Author
Xingyu Jin

Runtime: 40 ms
Memory Usage: 13.9 MB.
"""

def myAtoi(s) -> int:
    result = ""

    for c in s:
        if c == " " and result == "":
            continue
        if c in "0123456789":
            result += c
        elif c in "+-" and result == "":
            result += c
        else:
            break

    if result in "+-" or result == "":
        return 0

    result = int(result)
    if result > 2**31 - 1:
        return 2**31 - 1
    if result < -2**31:
        return -2**31
    return result
