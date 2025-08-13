"""
# -*- coding: utf-8 -*-
@File    : p0594_longest_harmonious_sussequence.py
@Author  : admin1
@Date    : 2025/8/13 21:04
@Description :
    594. 最长和谐子序列
    https://leetcode.com/problems/longest-harmonious-subsequence/
    和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。给你一个整数数组 nums ，请你在所有可能的 子序列 中找到最长的和谐子序列的长度。
    数组的 子序列 是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
    参考：哈希表统计每个数字出现的次数
"""
from collections import defaultdict


def find_lhs(nums: list[int]) -> int:
    # 统计每个元素出现频率
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    max_len = 0  # 最大长度
    for num in freq:
        if num + 1 in freq:  # 检查相邻数字是否存在
            # 计算和谐子序列长度
            curr_len = freq[num] + freq[num + 1]
            if curr_len > max_len:
                max_len = curr_len
    return max_len


"""
freq = defaultsect(int) 初始化字典后可以自动处理：
    当访问不存在的键时，自动创建该键并赋值为 0
    当更新不存在的键时，直接操作
"""
