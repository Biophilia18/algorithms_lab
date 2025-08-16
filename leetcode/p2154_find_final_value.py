"""
# -*- coding: utf-8 -*-
@File    : p2154_find_final_value.py
@Author  : admin1
@Date    : 2025/8/16 20:47
@Description :
    2154. 将找到的值乘以 2
    https://leetcode.com/problems/keep-multiplying-found-values-by-two/
    思路： 先用集合对数组去重，然后检查original是否在其中，如果在就*2后继续找
"""


def find_final_value(nums: list[int], original: int) -> int:
    nums_set = set(nums)
    while original in nums_set:  # 若存在第一次必然进入条件，返回的就不是原来的那个数了
        original *= 2
    return original
