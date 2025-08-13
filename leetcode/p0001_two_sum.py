"""
# -*- coding: utf-8 -*-
@File    : p0001_two_sum.py
@Author  : admin1
@Date    : 2025/8/12 9:52
@Description :
    1.两数之和
    https://leetcode.com/problems/two-sum/
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
    你可以按任意顺序返回答案。
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    :param nums: 给定数组
    :param target: 给定目标值
    :return: 返回构成目标值和的两数下标
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []