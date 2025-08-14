"""
# -*- coding: utf-8 -*-
@File    : p0888_fair_candy_swap.py
@Author  : admin1
@Date    : 2025/8/14 10:37
@Description :
    888.公平的糖果交换
    https://leetcode.com/problems/fair-candy-swap/
    爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 aliceSizes 和 bobSizes ，aliceSizes[i] 是爱丽丝拥有的第 i 盒糖果中的糖果数量，
    bobSizes[j] 是鲍勃拥有的第 j 盒糖果中的糖果数量。两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人
    拥有的糖果总数量是他们每盒糖果数量的总和。返回一个整数数组 answer，其中 answer[0] 是爱丽丝必须交换的糖果盒中的糖果的数目，
    answer[1] 是鲍勃必须交换的糖果盒中的糖果的数目。如果存在多个答案，你可以返回其中 任何一个 。题目测试用例保证存在与输入对应的答案。
    思路：计算出两人的糖果总数，交换后两人数量相等，假设两者交换的数量为x,y,交换后的糖果数量可以得到两者的关系
"""


def fair_candy_swap(alice_sizes: list[int], bob_sizes: list[int]) -> list[int]:
    """
    (sumA + sumB) / 2 两者交换后的平分
    sumA - x + y A减去交出去的加上B给的等于平分的量
    即  2(sumA - x + y) = sumA + sumB -->得出 x-y = (sumA - sumB) / 2
    """
    sumA, sumB = sum(alice_sizes), sum(bob_sizes)
    diff = (sumA - sumB) // 2  # 两者平分前后的差值
    setB = set(bob_sizes)  # 去重方便查找
    for x in alice_sizes:  # 遍历alice,计算差值对应bob
        y = x - diff
        if y in setB:  # 去重后在bob里找对应的值
            return [x, y]
