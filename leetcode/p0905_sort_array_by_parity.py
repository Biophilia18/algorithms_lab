"""
# -*- coding: utf-8 -*-
@File    : p0905_sort_array_by_parity.py
@Author  : admin1
@Date    : 2025/8/14 11:11
@Description :
    905.按奇偶排序数组
    https://leetcode.com/problems/sort-array-by-parity/
    给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。返回满足此条件的 任一数组 作为答案。
"""


def sort_array_by_parity(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1  # 初始化左右指针
    while left < right:
        # 左指针找第一个奇数（偶数不动）
        while left < right and nums[left] % 2 == 0:  # 条件不成立是则为奇数
            left += 1
        while left < right and nums[right] % 2 == 1:  # 条件不成立是则为偶数
            right -= 1
        # 交换位置：把左边的奇数换到右边，右边的偶数换到左边
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1  # 移动指针继续
            right -= 1

    return nums
