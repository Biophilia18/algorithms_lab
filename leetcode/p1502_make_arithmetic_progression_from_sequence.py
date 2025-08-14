"""
# -*- coding: utf-8 -*-
@File    : p1502_make_arithmetic_progression_from_sequence.py
@Author  : admin1
@Date    : 2025/8/14 17:26
@Description :
    1502. 判断能否形成等差数列
    https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
    给你一个数字数组 arr 。如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
    如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。
    思路：等差数列的特点就是响铃元素差值相等，计算
"""


def can_make_arithmetic_progression(arr: list[int]) -> bool:
    arr.sort()  # 排序
    differ = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):  # 遍历数组
        if arr[i + 1] - arr[i] != differ:  # 相邻差值变化证明不是等差
            return False
    return True
