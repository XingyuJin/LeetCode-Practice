"""
@Description
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

@Author: Xingyu Jin
"""

def minWindow(s: str, t: str) -> str:
    desired_count = {}
    for c in T:
        desired_count[c] = desired_count.get(c, 0) + 1

    head = 0
    cur_min = float('inf')
    window = (None, None)

    todo = len(desired_count)
    done = set()

    for i, c in enumerate(s):
        if c not in desired_count:
            continue

        desired_count[c] -= 1
        if desired_count[c] <= 0:
            done.add(c)

        while len(done) == todo:
            if cur_min > i - head + 1:
                cur_min = i - head + 1
                window = (head, i+1)

            head, dumped = head + 1, s[head]

            if dumped in desired_count:
                desired_count[c] += 1
                if desired_count[c] > 0:
                    done.remove(dumped)

    if cur_min == float('inf'):
        return ""
    return s[window[0]:window[1]]
