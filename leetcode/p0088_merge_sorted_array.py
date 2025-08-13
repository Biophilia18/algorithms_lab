"""
# -*- coding: utf-8 -*-
@File    : p0088_merge_sorted_array.py
@Author  : admin1
@Date    : 2025/8/11 16:03
@Description :
    88.合并两个有序数组
    https://github.com/halfrost/LeetCode-Go/tree/master/leetcode
    给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
    请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
    注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中
    前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
"""
import pytest


def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    """
    :param nums1: 目标数组
    :param m: nums1数组元素数量
    :param nums2: 待合并数组
    :param n: nums2数组元素数量
    :return:
    """

    sorted_list = []
    p1, p2 = 0, 0
    while p1 < m or p2 < n:
        if p1 == m:  # nums1处理完
            sorted_list.append(nums2[p2])
            p2 += 1
        elif p2 == n:  # nums2处理完
            sorted_list.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:  # nums1当前元素较小
            sorted_list.append(nums1[p1])
            p1 += 1
        else:
            sorted_list.append(nums2[p2])
            p2 += 1
    nums1[:] = sorted_list  # 结果复制到nums1


test_case = [
    ([0], 0, [1], 1, [1]),
    ([1, 2, 3, 0, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([2, 0], 1, [1], 1, [1, 2])
]


@pytest.mark.parametrize("nums1,m,nums2,n,expected", test_case)
def test_merge(nums1, m, nums2, n, expected):
    merge(nums1, m, nums2, n)
    assert nums1[:m+n] == expected
