"""
# -*- coding: utf-8 -*-
@File    : p0242_valid_anagram.py
@Author  : admin1
@Date    : 2025/8/13 15:25
@Description :
    242. 有效的字母异位词
    https://leetcode.com/problems/valid-anagram/
    给出 2 个字符串 s 和 t，如果 t 中的字母在 s 中都存在，输出 true，否则输出 false。
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):  # 检查长度
        return False
    char_cnt = {}
    # 统计s中的字符
    for char in s:
        if char in char_cnt:  # 如果字符已存在，计数+1；不存在则初始化为1
            char_cnt[char] += 1
        else:
            char_cnt[char] = 1
    # 验证t中的字符
    for char in t:
        if char not in char_cnt:  # 字符不存在s中
            return False
        char_cnt[char] -= 1  # 减少计数
        if char_cnt[char] < 0:  # # 计数变负数（再来一轮相同证明t中该字符多于s）
            return False
    return True
