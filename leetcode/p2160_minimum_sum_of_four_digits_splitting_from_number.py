"""
# -*- coding: utf-8 -*-
@File    : p2160_minimum_sum_of_four_digits_splitting_from_number.py
@Author  : admin1
@Date    : 2025/8/16 21:05
@Description :
    2160. 拆分数位后四位数字的最小和
    https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
    给你一个四位 正 整数 num 。请你使用 num 中的 数位 ，将 num 拆成两个新的整数 new1 和 new2 。new1 和 new2 中可以有 前导 0 ，
    且 num 中 所有 数位都必须使用。比方说，给你 num = 2932 ，你拥有的数位包括：两个 2 ，一个 9 和一个 3 。一些可能的 [new1, new2]
    数对为 [22, 93]，[23, 92]，[223, 9] 和 [2, 329] 。请你返回可以得到的 new1 和 new2 的 最小 和。
    思路：最小和的产生需要尽可能减小高位（十位和百位）的数字值。先取出整数的4个数位，然后将其中较大的两位放在两个数的十位，剩余的放在个位，
    和的表达 = 10*（最小+次小）+最大+次大
"""


def minimum_sum(num: int) -> int:
    digits = [int(d) for d in str(num)]  # 将整数拆为单个数字
    digits.sort()  # 升序排序
    # 前两个最小数字作十位，后两个作个位
    return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]
