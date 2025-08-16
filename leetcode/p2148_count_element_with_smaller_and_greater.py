"""
# -*- coding: utf-8 -*-
@File    : p2148_count_element_with_smaller_and_greater.py
@Author  : admin1
@Date    : 2025/8/16 20:41
@Description :
    2148. 元素计数
    https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/
    参考：先找出数组中的最小最大值min和max，然后遍历数组找到min<n<max的所有n即可
"""


def count_element(nums: list[int]) -> int:
    smallest = min(nums)
    largest = max(nums)
    res = 0
    for i in nums:
        if smallest < i < largest:
            res += 1
    return res
