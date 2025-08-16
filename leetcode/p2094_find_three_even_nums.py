"""
# -*- coding: utf-8 -*-
@File    : p2094_find_three_even_nums.py
@Author  : admin1
@Date    : 2025/8/16 14:41
@Description :
    2094.找出三位偶数
    https://leetcode.com/problems/finding-3-digit-even-numbers/
    统计输入数组中每个数字出现的次数，遍历所有100-998的偶数并将其分解为百十个位三个数
    然后验证这三个数在原数组的出现频次，收集所有可能的数字
"""
from collections import Counter


def find_even_nums(digits: list[int]) -> list[int]:
    # 1. 使用 Counter 统计原始数组中每个数字的出现次数
    # Counter 是字典的子类，用于计数可哈希对象
    # 例如：digits = [2,2,8,8,2] → orig_freq = {2:3, 8:2}
    orig_freq = Counter(digits)

    # 2. 准备结果列表
    result = []

    # 3. 遍历所有三位偶数（100 到 998，步长为 2）
    # 注意：range(start, stop, step) 包含 start，不包含 stop
    for num in range(100, 1000, 2):
        # 4. 分解数字为百位(a)、十位(b)、个位(c)
        # 例如：num = 228 → a=2, b=2, c=8
        a = num // 100  # 百位（整除100）
        b = (num // 10) % 10  # 十位（先整除10，再模10）
        c = num % 10  # 个位（模10）

        # 5. 创建当前数字的频率计数器
        # 使用列表 [a, b, c] 创建 Counter
        # 例如：a=2,b=2,c=8 → num_freq = {2:2, 8:1}
        num_freq = Counter([a, b, c])

        # 6. 验证当前数字是否有效
        valid = True
        # 遍历当前数字中的每个不同数字
        for digit in num_freq:
            # 6.1 检查当前数字在原始数组中是否存在且数量足够
            # orig_freq.get(digit, 0) 获取该数字在原始数组中的出现次数
            # 如果不存在则返回 0
            if num_freq[digit] > orig_freq.get(digit, 0):
                valid = False
                break  # 发现无效数字，提前终止检查

        # 7. 如果有效，加入结果列表
        if valid:
            result.append(num)

    # 8. 返回结果（由于遍历顺序是从小到大，结果自然有序）
    return result
