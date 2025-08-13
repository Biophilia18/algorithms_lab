"""
# -*- coding: utf-8 -*-
@File    : p0389_find_difference.py
@Author  : admin1
@Date    : 2025/8/13 17:40
@Description :
    389. 找不同
    https://leetcode.com/problems/find-the-difference/
    在找出只出现一次的元素时，异或运算的特性非常有用。如果一个元素在数组中出现两次，那么
    两次异或操作会使这个元素的二进制位变回0。只有出现一次的元素会保留下来。这就是为什么
    使用异或运算可以高效地找出只出现一次的元素。
"""


def dinf_the_difference(s: str, t: str) -> str:
    xor_res = 0
    for char in s:  # 遍历s字符串记录所有元素异或的值
        xor_res ^= ord(char)  # 字符转ascii码数字
    for char in t:  # 遍历t字符串异或
        xor_res ^= ord(char)
    return chr(xor_res)  # 最终结果即是多出来的字符
