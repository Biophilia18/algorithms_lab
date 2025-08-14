"""
# -*- coding: utf-8 -*-
@File    : p0747_largest_num_at_least_twice_of_others.py
@Author  : admin1
@Date    : 2025/8/14 10:16
@Description :
    747.至少是其他数字两倍的最大数
    https://leetcode.com/problems/largest-number-at-least-twice-of-others/
    给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍(第二大的数) 。
    如果是，则返回 最大元素的下标 ，否则返回 -1
    参考：动态维护找出最大值是第二大值，然后判断前者是后者的至少两倍
"""


def dominant_index(nums: list[int]) -> int:
    if len(nums) == 1:
        return -1
    max1, max2, idx = -1, -1, 0  # 初始化最大、第二大、最大值索引
    for i, num in enumerate(nums):
        if num > max1:
            max2 = max1  # 最大变第二大
            max1 = num  # 更新最大值
            idx = i  # 更新最大下标
        elif num > max2:
            max2 = num
    return idx if max1 >= 2 * max2 else -1
