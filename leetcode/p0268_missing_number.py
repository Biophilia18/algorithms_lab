"""
# -*- coding: utf-8 -*-
@File    : p0268_missing_number.py
@Author  : admin1
@Date    : 2025/8/13 16:38
@Description :
    268. 丢失的数字
    https://leetcode.com/problems/missing-number/
    给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
"""


def missing_number(nums: list[int]) -> int:
    # 数学解法，高斯公式求和在与数列之和对比，差值即为目标值
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)
