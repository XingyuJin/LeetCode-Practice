"""
@Description
Change Roman Number to Integer base 10

@Author
Xingyu Jin

Runtime: 48 ms, faster than 91.78% of Python3 LeetCode submissions
Memory Usage: 13.9 MB.
"""

def romanToInt(s: str) -> int:
    val_dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    sub_val = "IXC"
    sub_cond = {"I":"VX", "X":"LC", "C":"DM"}
    result = 0

    for i in range(len(s)-1):
        if s[i] in sub_val and s[i+1] in sub_cond[s[i]]:
            result -= val_dic[s[i]]
        else:
            result += val_dic[s[i]]

    return result+val_dic[s[-1]]
