"""
# -*- coding: utf-8 -*-
@File    : p0645_set_mismatch.py
@Author  : admin1
@Date    : 2025/8/14 9:20
@Description :
    645.错误的集合
    https://leetcode.com/problems/set-mismatch/
    集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致
    集合 丢失了一个数字 并且 有一个数字重复 。
    给定一个数组 nums 代表了集合 S 发生错误后的结果。请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回
    思路：哈希表（字典）法：记录每个数字出现次数，重复数字出现 2 次，缺失数字出现 0 次。
         异或法：利用异或性质找出重复和缺失的数字。
"""
from collections import defaultdict


def find_error_num_hash(nums: list[int]) -> list[int]:
    # freq = {}
    freq = defaultdict(int)  # 自动初始化为0
    duplicate = -1  # 重复标记位
    for n in nums:  # 记录并找出重复数字
        freq[n] += 1
        if freq[n] == 2:
            duplicate = n
    for i in range(1, len(nums) + 1):  # 找出缺失数字
        if i not in freq:
            return [duplicate, i]


def find_error_num_xor(nums: list[int]) -> list[int]:
    pass
    """理解有点复杂，待补充"""
