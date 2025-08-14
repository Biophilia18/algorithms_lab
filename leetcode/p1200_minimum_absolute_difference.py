"""
# -*- coding: utf-8 -*-
@File    : p1200_minimum_absolute_difference.py
@Author  : admin1
@Date    : 2025/8/14 16:39
@Description :
    1200. 最小绝对差
    https://leetcode.com/problems/minimum-absolute-difference/
    给你个整数数组 arr，其中每个元素都 不相同。请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
    每对元素对 [a,b] 如下：
    a , b 均为数组 arr 中的元素
    a < b
    b - a 等于 arr 中任意两个元素的最小绝对差
    思路：先排序（升），两两取数，计算差值，返回差值最小的所有数对 。贪心
"""


def minimum_abs_difference(arr: list[int]) -> list[list[int]]:
    arr.sort()  # 排序
    min_diff = float("inf")
    res = []
    for i in range(len(arr) - 1):  # 遍历相邻元素找最小差值
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            res = [[arr[i], arr[i + 1]]]  # 更新最小值同时重置结果
        elif diff == min_diff:
            res.append([arr[i], arr[i + 1]])  # 相同差值时追加
    return res


"""
float('inf') → 正无穷（找最小值的初始化常用）
float('-inf') → 负无穷（找最大值的初始化常用）
"""
