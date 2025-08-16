"""
# -*- coding: utf-8 -*-
@File    : p0015_sum_of_3_nums.py
@Author  : admin1
@Date    : 2025/8/16 9:51
@Description :
    15.三数之和
    https://leetcode.com/problems/3sum/
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时
    还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。注意：答案中不可以包含重复的三元组。
    参考：排序+双指+去重处理
        排序数组，方便使用双指针,去除重复元素
        固定一个数作为第一个元素
        使用双指针在剩余区间找两数之和
        跳过重复元素，避免重复解
"""


def three_sums(nums: list[int]) -> list[list[int]]:
    nums.sort()  # 排序数组
    res = []
    n = len(nums)
    for i in range(n - 2):  # 留出左右指针的位置
        if i > 0 and nums[i] == nums[i]:  # 跳过重复的第一个数 外循环固定一个nums[i]
            continue
        if nums[i] > 0:  # 提前结束，最小数大于0时无解
            break
        left, right = i + 1, n - 1  # 双指针初始化 nums[left],nums[right]一个重nums[i]的下一位开始，一个从末尾开始
        while left < right:  # 固定nums[i]后的内循环在剩下数字里寻找两数之和= -nums[i]
            total = nums[i] + nums[left] + nums[right]
            if total < 0:  # 和为负往右找大数
                left += 1
            elif total > 0:  # 何为正往左找小数
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])  # 符合条件的三元组
                while left < right and nums[left] == nums[left+1]:  # 排除相邻重复的元素,需要移动指针遇到不同的值
                    left += 1                                       # 当循环条件不成立时，指着指向最后一个重复值
                while left < right and nums[right] == nums[right+1]:  # 而这个值已经被使用，需要再移动位置指向下一个新位置不同的值
                    right -= 1
                left += 1  # 移动位置到重复值之外的新位置
                right -= 1
    return res
