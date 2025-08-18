"""
# -*- coding: utf-8 -*-
@File    : p0035_search_insert_postion.py
@Author  : admin1
@Date    : 2025/8/18 21:09
@Description :
    35. 搜索插入位置
    https://leetcode.com/problems/search-insert-position/
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    请必须使用时间复杂度为 O(log n) 的算法。
    参考：二分查找。先初始化左右指针，循环查找，处理找不到的情况
"""


def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # 找不到时left指向该插入的位置
