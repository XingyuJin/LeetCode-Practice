"""
@Description
Given two sorted integer arrays, destructively merge them into
one sorted array with no extra space.

@Author: Xingyu Jin

@Performance(on average):
Rumtime: 92 ms	Memory: 14.6 MB
"""

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    end = m + n - 1
    while m >= 0 and n >= 0:
        if nums2[n] >= nums1[m]:
            nums1[end] = nums2[n]
            n -= 1
        else:
            nums1[m], nums1[end] = nums1[end], nums1[m]
            m -= 1
        end -= 1