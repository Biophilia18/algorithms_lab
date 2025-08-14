"""
# -*- coding: utf-8 -*-
@File    : p1005_maximum_sum_of_array_after_k_negations.py
@Author  : admin1
@Date    : 2025/8/14 15:52
@Description :
    1005. K 次取反后最大化的数组和
    https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
    给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。重复这个过程恰好 k 次。
    可以多次选择同一个下标 i 。以这种方式修改数组后，返回数组 可能的最大和 。
    思路：使用贪心处理，优先取饭绝对值最大的负数（收益最大），取反一次能变相更新最小的元素，k次操作后（没负数），k为奇数取反最小的证书一次，偶数
    次取反0即可
"""


def largest_sum_after_k_negations(nums: list[int], k: int) -> int:
    nums.sort()  # 排序
    for i in range(len(nums)):  # 先取反负数
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
    if k % 2 == 1:
        nums.sort()  # 获取最小的正数（需要包含前面已取反得到的正数）
        nums[0] = -nums[0]
    return sum(nums)
