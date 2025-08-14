"""
# -*- coding: utf-8 -*-
@File    : p0977_squares_of_sorted_array.py.py
@Author  : admin1
@Date    : 2025/8/14 15:07
@Description :
    977.有序数组的平方
    https://leetcode.com/problems/squares-of-a-sorted-array/
    给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序
    思路：给出的数组已经排序，平方后的最大值一定出现在数组两端（有负数时绝对值最大）。用双指针一前一后往中间移动，从数组末尾开始填充，依次放
    入当前最大的平方值
"""


def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    left, right = 0, n - 1  # 初始化指针
    res = [0] * n
    idx = n - 1  # 从末尾开始填充
    while left <= right:
        left_val = nums[left] ** 2
        right_val = nums[right] ** 2
        if left_val > right_val:
            res[idx] = left_val
            left += 1
        else:
            res[idx] = right_val
            right -= 1
        idx -= 1
    return res
