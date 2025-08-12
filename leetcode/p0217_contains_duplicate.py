"""
# -*- coding: utf-8 -*-
@File    : p0217_contains_duplicate.py
@Author  : admin1
@Date    : 2025/8/12 8:28
@Description :
    217. 存在重复元素
    https://leetcode.com/problems/contains-duplicate/
    给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
"""
import time
from random import randint


def contains_duplicate_dict(nums: list[int]) -> bool:
    # 使用字典标记
    dt = {}
    for num in nums:  # 遍历
        if num in dt:  # 存在则证明重复
            return True
        dt[num] = True  # 不存在便加入字典进行
    return False  # 遍历完都没有证明无重复


def contains_duplicate_set(nums: list[int]) -> bool:
    # 利用集合去重性质比较两者长度即可
    return len(nums) != len(set(nums))


def time_calculate(func, data):
    start = time.time()
    result = func(data)
    duration = time.time() - start
    print(f"{func.__name__}: {result} ({duration:.8f})s")


# test_data = [randint(0, 100000) for _ in range(100000)] # 预期有重复
test_data = [i for i in range(100000)]  # 预期无重复
test_data.append(test_data[0])
time_calculate(contains_duplicate_dict, test_data)
time_calculate(contains_duplicate_set, test_data)

"""
得出结论：在预期有重复的情况下，字典处理更高效，处理到重复元素时即可提前反回，而集合需要完整处理并且判断两者长度是否一致
预期没有重复的情况下，集合方法更快速。而在不确定的情况下使用集合更简洁
"""