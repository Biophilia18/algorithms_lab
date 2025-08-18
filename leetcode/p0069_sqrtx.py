"""
# -*- coding: utf-8 -*-
@File    : p0069_sqrtx.py
@Author  : admin1
@Date    : 2025/8/18 21:23
@Description :
    69. x 的平方根
    https://leetcode.com/problems/sqrtx/
    给你一个非负整数 x ，计算并返回 x 的 算术平方根 。由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
    注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
    参考：使用牛顿迭代法对x求解平方根
"""


def my_sqrt(x: int) -> int:
    if x == 0:
        return 0
    y = x
    while True:
        next_y = (y + x / y) / 2
        if abs(next_y - y) < 1e-7:  # 检查是否收敛
            break
        y = next_y
    return int(y)  # 返回整数部分
