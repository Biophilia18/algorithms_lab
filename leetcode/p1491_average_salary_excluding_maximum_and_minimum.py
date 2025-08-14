"""
# -*- coding: utf-8 -*-
@File    : p1491_average_salary_excluding_maximum_and_minimum.py
@Author  : admin1
@Date    : 2025/8/14 17:17
@Description :
    1491. 去掉最低工资和最高工资后的工资平均值
    https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
    思路：动态维护两个最值的同时并求和
"""


def average(salary: list[int]) -> float:
    max_val = float("-inf")
    min_val = float("inf")  # 初始化最值
    total = 0
    for s in salary:
        total += s
        if s > max_val:
            max_val = s
        if s < min_val:
            min_val = s
    return (total - min_val - max_val) / (len(salary) - 2)
