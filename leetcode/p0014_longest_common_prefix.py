"""
# -*- coding: utf-8 -*-
@File    : p0014_longest_common_prefix.py
@Author  : admin1
@Date    : 2025/8/12 11:44
@Description :
    14. 最长公共前缀
    https://leetcode.com/problems/longest-common-prefix/
    编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
    示例 ：
    输入：strs = ["flower","flow","flight"]
    输出："fl"
"""


def longest_common_prefix(string: list[str]) -> str:
    if not string:
        return ""
    prefix = string[0]  # 用第一个元素起头
    for i in range(1, len(string)):  # 遍历其他字符串
        j = 0  # 每一个字符串下标都重置
        while j < len(prefix):  # 遍历字符串的每个字符
            if j >= len(string[i]) or string[i][j] != prefix[j]:
                # 当前字符串小于初始前缀 或者 当前字符不匹配
                prefix = prefix[:j]   # 截断字符串
                break
            j += 1

    return prefix


s = ["flower", "flow", "flight"]
print(longest_common_prefix(s))
