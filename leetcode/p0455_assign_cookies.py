"""
# -*- coding: utf-8 -*-
@File    : p0455_assign_cookies.py
@Author  : admin1
@Date    : 2025/8/13 18:20
@Description :
    455. 分发饼干
    https://leetcode.com/problems/assign-cookies/
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们
    满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得
    到满足。你的目标是满足尽可能多的孩子，并输出这个最大数值。
    参考：这是一道典型的简单贪心题。贪心题一般都伴随着排序。将 g[] 和 s[] 分别排序。按照最难满足的小朋友开始给饼干，依次往下满足，最终能满
    足的小朋友数就是最终解。
"""


def find_content_children(g: list[int], s: list[int]) -> int:
    # 先对两数组排序
    g.sort()  # 孩子胃口排序
    s.sort()  # 饼干尺寸排序
    child = 0  # 满足的孩子数量（也是指针)
    cookie = 0  # 当前尝试的饼干索引
    while child < len(g) and cookie < len(s):  # 双指针遍历
        if s[cookie] >= g[child]:  # 当前饼干满足当前孩子
            child += 1  # 满足一个孩子
        cookie += 1  # 无论是否满足，饼干都只使用一次，并尝试下一块饼干
    return child  # 返回满足的孩子总数
