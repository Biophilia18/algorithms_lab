"""
# -*- coding: utf-8 -*-
@File    : p2231_swap_digits_to_get_largest_number.py
@Author  : admin1
@Date    : 2025/8/18 17:46
@Description :
    2231. 按奇偶性交换后的最大数字
    https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
    给你一个正整数 num 。你可以交换 num 中 奇偶性 相同的任意两位数字（即，都是奇数或者偶数）。
    返回交换 任意 次之后 num 的 最大 可能值。
    参考：由题可知所有奇数偶数的数字都可以自由排列，最优策略是先将数字的字符提取出来，将奇数偶数数字分别降序排列，从排序后的数字序列中依次选取最大值
"""


def largest_integer(num: int) -> int:
    s = str(num)
    odd = []  # 奇数
    even = []  # 偶数
    for char in s:  # 遍历每一位数字并分组
        digit = int(char)
        if digit % 2 == 0:
            even.append(char)
        else:
            odd.append(char)
    odd.sort(reverse=True)
    even.sort(reverse=True)  # 降序排列
    res = []
    i, j = 0, 0  # 奇偶指针
    for char in s:
        digit = int(char)
        if digit % 2 == 0:
            res.append(str(even[j]))
            j += 1
        else:
            res.append(str(odd[i]))
            i += 1
    return int(''.join(res))
