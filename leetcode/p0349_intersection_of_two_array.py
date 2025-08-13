"""
# -*- coding: utf-8 -*-
@File    : p0349_intersection_of_two_array.py
@Author  : admin1
@Date    : 2025/8/13 17:21
@Description :
    349. 两个数组的交集
    https://leetcode.com/problems/intersection-of-two-arrays/
    给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
"""


def intesrsection(nums1: list[int], nums2: list[int]) -> list[int]:
    num_dict = []
    for num in nums1:
        num_dict[num] = True  # 字典标记数组1所有元素
    result = []
    for num in nums2:
        if num in num_dict:  # 检查是否为共同元素
            result.append(num)  # 添加到结果
            del num_dict[num]  # 删除防止重复添加
    return result
