"""
# -*- coding: utf-8 -*-
@File    : basic_search_and_sort.py
@Author  : admin1
@Date    : 2025/8/13 13:42
@Description : 顺序查找、二分查找、冒泡排序、选择排序、快速排序、递归算法
"""


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
    pass  # 后续补充


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


test_data = [22, 1, 34, 55, 63, 2, 89, 17, 100, 3, 24]
print(bubble_sort(test_data))
print(quick_sort(test_data))
print(selection_sort(test_data))