"""
# -*- coding: utf-8 -*-
@File    : p1464_maximum_product_of_two_elements_in_array.py
@Author  : admin1
@Date    : 2025/8/14 17:04
@Description :
    1464. 数组中两元素的最大乘积
    https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
    给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。
    请你计算并返回该式的最大值。
    思路:动态维护最大值和第二大的值,结束后返回这两数减1的乘积
"""


def max_product(nums: list[int]) -> int:
    max1 = max2 = float("-inf")  # 初始化为负无穷
    for num in nums:
        if num > max1: # 每轮对比大小进行动态维护
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return (max1 - 1) * (max2 - 1)
