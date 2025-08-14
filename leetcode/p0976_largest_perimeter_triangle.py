"""
# -*- coding: utf-8 -*-
@File    : p0976_largest_perimeter_triangle.py
@Author  : admin1
@Date    : 2025/8/14 14:30
@Description :
    976.三角形的最大周长
    https://leetcode.com/problems/largest-perimeter-triangle/
    给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。
    如果不能形成任何面积不为零的三角形，返回 0。
    思路：根据给出的边长数组三角形构成条件：对于三个边a<=b<=c,必须满足a+b>c。贪心思路：排序后取最大的三个数尝试（周长最大），如果不满足条件，固定
    较小的两个数，往前取除这三个数的最大数。即对于排序数组nums(升序），选择连续的三个数：nums[i]<=nums[j]<=nums[k],如果nums[i]+num[j]
    > nums[k]不成立，则尝试往前移动指针选择对于小于i的m尝试
"""


def sorted_perimeter(nums: list[int]) -> int:
    nums.sort()  # 升序排列
    n = len(nums)
    for i in range(n - 1, 1, -1):  # 从后往前每次取三个数
        if nums[i - 2] + nums[i - 1] > nums[i]:
            return nums[i - 2] + nums[i - 1] + nums[i]
    return 0
