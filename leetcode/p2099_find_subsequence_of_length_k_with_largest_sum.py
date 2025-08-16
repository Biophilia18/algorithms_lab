"""
# -*- coding: utf-8 -*-
@File    : p2099_find_subsequence_of_length_k_with_largest_sum.py
@Author  : admin1
@Date    : 2025/8/16 19:45
@Description :
    2099.找到和最大的长度为K的子序列
    https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
    给你一个整数数组 nums 和一个整数 k 。你需要找到 nums 中长度为 k 的 子序列 ，且这个子序列的 和最大 。
    请你返回 任意 一个长度为 k 的整数子序列。
    子序列 定义为从一个数组里删除一些元素后，不改变剩下元素的顺序得到的数组。
    参考：子序列和最大肯定是由最大的k个元素构成，需要保存这个k个元素按原来的顺序排列，有多个重复值的时候
    保留在原数组中出现的顺序
"""


def max_sum_subsequence(nums: list[int], k: int) -> list[int]:
    # 创建带索引的数组 [(数值，索引)] enumerate() → 返回 (index, value)
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    # 按数值降序排序，数值相同时按索引升序排序，这样确保相同数值的元素按原顺序处理
    indexed_nums.sort(key=lambda x: (-x[0], x[1]))
    # 取前k个最大的元素
    top_k = indexed_nums[:k]
    # 按元素索引牌小，回复在原数组中的顺序
    top_k.sort(key=lambda x: x[1])
    # 提取数值形成子序列
    return [num for num, idx in top_k]

