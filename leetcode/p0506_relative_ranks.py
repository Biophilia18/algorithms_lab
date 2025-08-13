"""
# -*- coding: utf-8 -*-
@File    : p0506_relative_ranks.py
@Author  : admin1
@Date    : 2025/8/13 18:47
@Description :
    506.相对名次
    https://leetcode.com/problems/relative-ranks/
    给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。
    运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：
    名次第 1 的运动员获金牌 "Gold Medal" 。
    名次第 2 的运动员获银牌 "Silver Medal" 。
    名次第 3 的运动员获铜牌 "Bronze Medal" 。
    从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
    使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。
    参考：用 字典（map) 记录原来 score 中元素对应的坐标，然后对 score 进行排序，对排序后的元素我们通过 map 就可以知道它排的名次
"""


def find_relative_ranks(score: list[int]) -> list[str]:
    # 用字典记录原始分数和索引
    score_dict = {}
    for idx, scr in enumerate(score):
        score_dict[scr] = idx
    sorted_scr = sorted(score, reverse=True)  # 降序排序
    result = [""] * len(score)  # 初始化结果数组,避免动态扩容
    for rank, s in enumerate(sorted_scr):  # 分配名词
        # 找到当前分数对应的原始位置
        origin_idx = score_dict[s]
        if rank == 0:  # 根据名次分配奖牌
            result[origin_idx] = "Gold Medal"
        elif rank == 1:
            result[origin_idx] = "Silver Medal"
        elif rank == 2:
            result[origin_idx] = "Bronze Medal"
        else:
            result[origin_idx] = str(rank + 1)

    return result


"""
补充:enumerate(iterable, start=0) 是Python内置函数，用于：
    给可迭代对象添加计数器
    返回(索引, 元素)的元组序列,简化索引获取
    iterable：任何可迭代对象（列表、元组、字符串等）
    start：计数起始值（默认为0）
"""
