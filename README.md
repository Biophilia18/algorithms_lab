# 算法学习实验室

> 使用python 学习并尝试解决LeetCode 算法问题

## 数据结构

- Array

- String

- Two pointers

- Binary Search

- Sorting

## 动态维护

动态维护是一高效的算法设计思想，核心是在**单次遍历数据的过程中实时更新关键状态**，避免重复计算或存储全部数据。在处理大规模数据流或者需要高效计算的问题中尤为重要。

**核心思想**：

1.状态精简：只需维护解决问题所需的最小状态集

2.实时更新：在数据到达时立即更新状态

3.增量计算：基于前一个状态计算新状态，避免重复计算

4.空间优化：通常使用常数空间（**O(1)**）

**典型应用场景：**

1.极值统计

2.TOP K元素

3.滑动窗口统计

4.数据流中位数

5.连续序列问题

## 贪心策略

贪心策略（Greedy Strategy），也称为贪心算法，是一种**在每一步选择中都采取当前看起来最优的选择**，从而希望最终得到全局最优解的算法或策略。它并不考虑整体的最优，而是每一步都追求局部最优，希望这些局部最优的选择能最终导向全局最优 

## 已完成题目

| 题号   | 题目名称          | 难度  | 代码                                                                                                                                   | -   |
| ---- | ------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------ | --- |
| 0088 | 合并两个有序数组      | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p088_merge_sorted_array.py)                                |     |
| 0217 | 存在重复元素        | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0217_contains_duplicate.py)                               |     |
| 0009 | 回文数           | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0009_palindrome_number.py)                                |     |
| 0013 | 罗马字转数字        | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0013_roman_to_int.py)                                     |     |
| 0014 | 最长的公共前缀       | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0014_longest_common_prefix.py)                            |     |
| 0001 | 两数之和          | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0001_two_sum.py)                                          |     |
| 0169 | 多数元素（众数）      | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0169_majority_element.py)                                 |     |
| 0242 | 有效的字母异位次      | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0242_valid_anagram.py)                                    |     |
| 0268 | 丢失的数字         | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0268_missing_number.py)                                   |     |
| 0349 | 两个数组的交集       | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0349_intersection_of_two_array.py)                        |     |
| 0389 | 找不同           | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0389_find_difference.py)                                  |     |
| 0414 | 第三大的数         | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0414_third_maximum_number.py)                             |     |
| 0455 | 分发饼干          | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0455_assign_cookies.py)                                   |     |
| 0506 | 相对名次          | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0506_relative_ranks.py)                                   |     |
| 0561 | 数组拆分          | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0561_array_partition.py)                                  |     |
| 0594 | 最长和谐子列        | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0594_longest_harmonious_sussequence.py)                   |     |
| 0628 | 三个数的最大乘积      | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0628_maximum_product_of_three_numbers.py)                 |     |
| 0645 | 错误的集合         | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0645_set_mismatch.py)                                     |     |
| 0747 | 至少是其他数字两倍的最大数 | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0747_largest_num_at_least_twice_of_others.py)             |     |
| 0888 | 公平的糖果交换       | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0888_fair_candy_swap.py)                                  |     |
| 0905 | 按奇偶排序数组       | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0905_sort_array_by_parity.py)                             |     |
| 0976 | 三角形的最大周长      | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0976_largest_perimeter_triangle.py)                       |     |
| 0977 | 有序数组的平方       | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0977_squares_of_sorted_array.py.py)                       |     |
| 1005 | K次取反后最大化的数组和  | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p1005_maximum_sum_of_array_after_k_negations.py)           |     |
| 1051 | 高度检查器         | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p1051_height_checkr.py)                                    |     |
| 1200 | 最小绝对差         | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p1200_minimum_absolute_difference.py)                      |     |
| 1464 | 数组中量元素的最大乘积   | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p1464_maximum_product_of_two_elements_in_array.py)         |     |
| 1491 | 去掉最低最高的平均工资   | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p1491_average_salary_excluding_maximum_and_minimum.py)     |     |
| 1502 | 判断能否形成等差数列    | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p1502_make_arithmetic_progression_from_sequence.py)        |     |
| 1913 | 两个数对之间最大的乘积   | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p1913_maximum_product_of_two_pairs.py)                     |     |
| 0015 | 三数之和          | 中等  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0015_sum_of_3_nums.py)                                    |     |
| 2094 | 找出3位偶数        | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p2094_find_three_even_nums.py)                             |     |
| 2099 | 找到和最大的长为K的子序列 | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p2099_find_subsequence_of_length_k_with_largest_sum.py)    |     |
| 2144 | 打折购买糖果的最小开销   | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p2144_minimum_cost_of_buying_candies.py)                   |     |
| 2148 | 元素计数          | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p2148_count_element_with_smaller_and_greater.py)           |     |
| 2154 | 找到的值乘以2       | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p2154_find_final_value.py)                                 |     |
| 2160 | 拆分数位后4位数字的最小和 | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p2160_minimum_sum_of_four_digits_splitting_from_number.py) |     |
| 2231 | 按奇偶性交换后的最大数字  | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p2231_swap_digits_to_get_largest_number.py)                |     |
| 0035 | 搜索插入位置        | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0035_search_insert_postion.py)                            |     |
| 0069 | 求平方根          | 简单  | [python](https://github.com/Biophilia18/algorithms_lab/tree/main/leetcode/p0069_sqrtx.py)                                            |     |


