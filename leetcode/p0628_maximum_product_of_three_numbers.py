"""
# -*- coding: utf-8 -*-
@File    : p0628_maximum_product_of_three_numbers.py
@Author  : admin1
@Date    : 2025/8/14 8:44
@Description :
    628. 三个数的最大乘积
    https://leetcode.com/problems/maximum-product-of-three-numbers/
    给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
    参考：挑出 3 个数组成乘积最大值，必然是一个正数和二个负数，或者三个正数。那么选出最大的三个数和最小的二个数，对比一下就可以求出最大值。即不用
    排序，使用线性扫描直接得出这5个数
"""
from _testcapi import INT_MAX, INT_MIN


def maximum_product(nums: list[int]) -> int:
    max1 = max2 = max3 = INT_MIN  # 初始化最大值和最小值,分别为相反的值方便判断开始
    min1 = min2 = INT_MAX
    # 扫描更新最大最小值
    for num in nums:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min1 = num
    candidate1 = max1 * max2 * max3  # 全是正数、负数的情况
    candidate2 = min1 * min2 * max1  # 有正有负
    return max(candidate1, candidate2)


"""
线性扫描是一种在单次遍历中维护多个关键值的算法思想。通过动态更新几个变量来
记录数据流中的关键信息，避免对整个数据集进行排序(O(nlogn)),实现O(n)时间复杂度
和O(1)的空间复杂度优化
适用于同时获取多个极值的问题：
1.找出Top K元素（K固定且较小）
2.统计类问题（最大/最小K个数的组合）
3.数据流处理（无法存储全部数据时）
"""
