"""
# -*- coding: utf-8 -*-
@File    : p0414_third_maximum_number.py
@Author  : admin1
@Date    : 2025/8/13 17:59
@Description :
    414. 第三大的数
    https://leetcode.com/problems/third-maximum-number/
    给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
    思路：动态维护 3 个最大值即可。注意数组中有重复数据的情况。如果只有 2 个数或者 1 个数，则返回 2 个数中的最大值即可。
"""


def third_max(nums: list[int]) -> int:
    # 初始化三个变量为None
    first = second = third = None
    for num in nums:
        # 跳过重复步骤
        if num == first or num == second or num == third:
            continue
        # 更新三个最大值
        if first is None or num > first:  # 新选手挑战金牌
            third = second  # 原银牌变铜牌
            second = first  # 原金牌变银牌
            first = num     # 新选手拿金牌
        elif second is None or num > second:  # 新选手挑战银牌
            third = second  # 原银牌变铜牌
            second = num    # 新选手拿银牌
        elif third is None or num > third:  # 新选手挑战铜牌
            third = num  # 新选手拿铜牌
    return third if third is not None else first  # 第三大值不存在就返回最大
