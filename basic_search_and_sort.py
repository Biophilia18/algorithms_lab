"""
# -*- coding: utf-8 -*-
@File    : basic_search_and_sort.py
@Author  : admin1
@Date    : 2025/8/13 13:42
@Description : 顺序查找、二分查找、冒泡排序、选择排序、快速排序、递归算法
"""
import functools
import random
import time


# 计时器
def timer(func):
    """测量函数执行时间"""

    @functools.wraps(func)  # 保留原函数信息（函数名，文档字符）
    def warpper(*args, **kwargs):
        start = time.perf_counter()  # 高精度时间
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"函数 {func.__name__} 执行时间： {end - start:.6f} 秒")
        return res, end - res

    return warpper


def sequential_search(arr, target):
    """
    顺序查找算法: 时间复杂度：O(n) - 最坏情况下需要遍历整个数组
    :param arr: 待搜索的列表
    :param target: 要查找的目标值
    :return:  目标值在列表中的索引，如果未找到则返回 -1
    """
    if not arr:
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    二分查找（要求数组已排序）：时间复杂度：O(log n) - 每次将搜索范围减半
    :param arr: 已排序列表
    :param target: 要查找的目标值
    :return: 目标值在列表中的索引，如果没找到则返回 -1
    """
    if not arr:
        return -1
    left, right = 0, len(arr) - 1  # 初始化左右指针
    while left <= right:
        #  计算中间位置
        mid = (left + right) // 2
        if arr[mid] == target:  # 中间值等于目标值返回
            return mid
        elif arr[mid] < target:  # 中间值小于目标值，从右半部分继续查找
            left = mid + 1
        else:  # 中间值大于目标值，从左半部分继续查找
            right = mid - 1

    return -1  # 找不到


def bubble_sort(arr):
    """
    冒泡排序算法：时间复杂度：O(n²) - 嵌套循环遍历所有元素
    :param arr: 待排序列表
    :return: 排序后列表
    """
    n = len(arr)
    for i in range(n):
        swapped = False  # 设置标志位
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换
                swapped = True
        if not swapped:  # 未交换证明排序结束
            break
    return arr


def selection_sort(arr):
    """
    选择排序： 时间复杂度：O(n²) - 每次找到最小元素
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        min_idx = i  # 假设当前位置是最小元素
        for j in range(i + 1, n):  # 在剩余元素中查找实际最小值
            if arr[j] < arr[min_idx]:
                min_idx = j  # 更新最小值下标
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 将找到的最小值与当前值交换
    return arr


def quick_sort(arr):
    """
    快速排序：时间复杂度：平均情况：O(n log n) 最坏情况：O(n²)（当分区不平衡时）
    :param arr:
    :return:
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择中间元素为基准值
    # 分区操作
    left = [x for x in arr if x < pivot]  # 小于基准值的元素
    middle = [x for x in arr if x == pivot]  # 等于基准值的元素
    right = [x for x in arr if x > pivot]  # 大于基准值的元素
    return quick_sort(left) + middle + quick_sort(right)  # 递归排序左右分区的元素然后合并结果


def quick_sort_optimize(arr):
    """优化点：原地分区快排，区别于递归调用,
    优化哨兵划分的基准数选取策略，选取首中尾三个元素的中位数作为基准数，提供算法稳定性
    """

    def _sort(low, high):  # 辅助递归函数
        if low >= high:  # 递归停止条件
            return
        mid = (low + high) // 2
        pivot_idx = _median_three(arr, low, mid, high)  # 选择基准
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]  # 基准值换到最左侧

        partition_idx = _partition(low, high)  # 哨兵分区
        _sort(low, partition_idx - 1)  # 递归排序左右分区，左小右大
        _sort(partition_idx + 1, high)

    def _median_three(arr, a, b, c):  # 返回三个索引里的中位数
        x, y, z = arr[a], arr[b], arr[c]
        # 确定中位数位置
        if (x <= y <= z) or (z <= y <= x):
            return b
        if (y <= x <= z) or (z <= x <= y):
            return a
        return c

    def _partition(low, high):  # 分区操作封装，返回分区完成的分区点
        pivot = arr[low]
        left, right = low, high  # 初始化左右指针从左右边界开始
        while left < right:
            while left < right and arr[right] >= pivot:  # 遇到大的继续左移
                right -= 1
            while left < right and arr[left] <= pivot:  # 遇到小的继续右移
                left += 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]  # 交换左右指针的元素
        arr[low], arr[right] = arr[right], arr[low]
        return right

    _sort(0, len(arr) - 1)  # 对整个数组开始排序
    return arr


def builtin_sort(arr):  # 内置排序
    return sorted(arr)


def factorial(n):
    """
    递归算法计算阶乘：时间复杂度：O(n) - 递归深度为n
    :param n: 非负整数
    :return: n的阶乘
    """
    if n == 0:  # 基本情况 0! = 1
        return 1
    else:
        return factorial(n - 1) * n


def fibonacci(n):
    """
    递归计算斐波那契数列：时间复杂度：O(2^n) - 指数级（实际应用中通常使用迭代或动态规划优化）
    :param n: 非负整数
    :return: 第n个斐波那契数
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# test_data = [22, 1, 34, 55, 63, 2, 89, 17, 100, 3, 24]
# print(bubble_sort(test_data))
# print(quick_sort(test_data))
# print(selection_sort(test_data))


def test_performance_fixed():
    # sizes = [1000, 3000, 5000, 10000]
    sizes = [10000, 100000, 1000000, 10000000]
    results = []

    print("测试中... 请耐心等待大数组测试")

    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]

        start = time.time()
        builtin_sort(data.copy())
        sort_time = time.time() - start

        # start = time.time()
        # selection_sort(data.copy())
        # select_time = time.time() - start
        select_time = 1
        #
        # start = time.time()
        # bubble_sort(data.copy())
        # buble_time = time.time() - start
        buble_time = 1
        #
        # # 测试简单快排
        # start = time.time()
        # quick_sort(data.copy())
        # simple_time = time.time() - start
        simple_time = 1
        #
        # # 测试优化快排
        # start = time.time()
        # quick_sort_optimize(data.copy())
        # optimized_time = time.time() - start
        optimized_time = 1

        # improvement = (simple_time - optimized_time) / simple_time * 100
        results.append((size, sort_time, select_time, buble_time, simple_time, optimized_time))
        # results.append((size, sort_time))

    print("\n修复后性能对比:")
    print("数据量   | 内置排序     | 选择排序    | 冒泡排序    |   简单快排     | 优化快排     | 对比内置")
    print("--------|------------|----------|-----------|-----------|----------|---------")
    for size, sort_time, select_time, buble_time, st, ot in results:
        print(f"{size:7} | {sort_time:.6f}s  | {select_time:.6f}s | {buble_time:.6f}s  | {st:.6f}s| {ot:.6f}s  | --")
