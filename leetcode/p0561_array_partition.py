"""
# -*- coding: utf-8 -*-
@File    : p0561_array_partition.py
@Author  : admin1
@Date    : 2025/8/13 20:46
@Description :
    561.数组拆分
    https://leetcode.com/problems/array-partition/
    给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的
    数对最小值 min(ai, bi) 的总和最大。返回该 最大总和 。
    参考：贪心算法
"""


def array_partition(nums: list[int]) -> int:
    # 排序数组（从小到大）
    nums.sort()
    # 遍历偶数位索引
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]
    return total


"""
要使得总和最大，就需要每个数对中的较小值尽可能大
后续补充贪心算法的具体分析
"""
