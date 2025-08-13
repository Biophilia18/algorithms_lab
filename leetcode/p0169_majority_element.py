"""
# -*- coding: utf-8 -*-
@File    : p0169_majority_element.py
@Author  : admin1
@Date    : 2025/8/12 18:03
@Description :
    169.多数元素
    https://leetcode.com/problems/majority-element/
    给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。

    解答：使用摩尔投票法解决多数元素，
    可以在O(n)时间复杂度和O(1)空间复杂度内高效找出数组中出现次数超过一半的元素
    [Boyer-Moore Majority Vote Algorithm](https://www.zhihu.com/question/49973163/answer/235921864)
"""


def majority_element(nums: list[int]) -> int:
    if not nums:
        return None
    cnt = 0  # 候选元素计数器
    candidate = None  # 当前候选元素
    for num in nums:
        if cnt == 0:
            candidate = num
        cnt += (1 if num == candidate else -1)
    return candidate
