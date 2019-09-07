"""
@Description
Find the length of the longest substring without repeating characters.

@Author
Xingyu Jin

Runtime: 52 ms, faster than 97.56% of Python3 LeetCode submissions
Memory Usage: 13.9 MB.
"""

def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        cur_max = 0

        for fast in range(len(s)) :
            if (s[fast] in s[slow:fast]):
                if fast - slow > cur_max:
                    cur_max = fast - slow
                while (s[slow] != s[fast]):
                    slow += 1
                slow += 1
                fast -= 1

        if len(s) - slow > cur_max:
            cur_max = len(s) - slow
        return cur_max
