"""
# -*- coding: utf-8 -*-
@File    : p1051_height_checkr.py
@Author  : admin1
@Date    : 2025/8/14 16:22
@Description :

    学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 非递减 的高度顺序排成一行。
    排序后的高度情况用整数数组 expected 表示，其中 expected[i] 是预计排在这一行中第 i 位的学生的高度（下标从 0 开始）。
    给你一个整数数组 heights ，表示 当前学生站位 的高度情况。heights[i] 是这一行中第 i 位学生的高度（下标从 0 开始）。
    返回满足 heights[i] != expected[i] 的 下标数量 。
    思路：贪心 不模拟每次交换，直接算出最终结果，用最少次数移动即一次移动就让他在该在的位置
"""


def height_checker(height: list[int]) -> int:
    expected = sorted(height)  # 最终的正确位置
    cnt = 0
    for h1, h2 in zip(height, expected):
        if h1 != h2:  # 前后对比谁移动就计数
            cnt += 1
    return cnt


"""
sort()和sorted()的区别：前者在原地排序会改变原有数据，后者返回一个新的排序好的数据，不操作原数据
zip(iter1, iter2, ...)用于将多个可迭代对象（如列表、元组、字符串等）中的元素按顺序"打包"成一个个元组，最终
返回一个迭代器。它在处理并行遍历多个序列时非常高效
a = [1, 2, 3]
b = ['x', 'y', 'z']
print(list(zip(a, b)))
# [(1, 'x'), (2, 'y'), (3, 'z')]
"""
