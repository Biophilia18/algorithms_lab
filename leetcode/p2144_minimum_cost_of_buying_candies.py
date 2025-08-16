"""
# -*- coding: utf-8 -*-
@File    : p2144_minimum_cost_of_buying_candies.py
@Author  : admin1
@Date    : 2025/8/16 20:26
@Description :
    2144. 打折购买糖果的最小开销
    https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
    参考：贪心策略：尽可能让贵的糖果被支付，让较便宜的免费送。即三个它能糖果一组送最便宜的那个。先降序排序，三个一组，支付前两个糖果，剩下一个免费
"""


def minimum_cost(cost: list[int]) -> int:
    cost.sort(reverse=True)  # 降序排序
    total = 0
    for i in range(len(cost)):  # 遍历糖果价格
        if (i + 1) % 3 == 0:  # 三个一组，跳过最后一个，索引2,5,8……
            continue
        total += cost[i]  # 计算其他糖果的费用
    return total
