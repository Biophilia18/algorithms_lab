"""
# -*- coding: utf-8 -*-
@File    : p0009_palindrome_number.py
@Author  : admin1
@Date    : 2025/8/12 10:08
@Description :
    9.回文数
    https://leetcode.com/problems/palindrome-number/
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    例如，121 是回文，而 123 不是。
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if x < 10:
        return True
    arr = []
    while x > 0:
        arr.append(x % 10)
        x //= 10
    # print(arr)
    n = len(arr)
    phead = 0  # 指向头
    ptail = n - 1  # 指向末尾
    while phead <= ptail:
        if arr[phead] != arr[ptail]:
            return False
        phead += 1
        ptail -= 1
    return True


f = is_palindrome(-10)
print(f)
