# -*- coding:utf-8 -*-
# binary search
def super_root(num):
    result = 0
    base = 1.0
    while not num - 0.001 < result**result < num + 0.001:
        if result**result < num:
            result += base
        else:
            base /= 2
            result -= base
    return result


def super_rootv(y):
    I, x = [1, 10], 1
    while abs(x**x - y) > 1e-3: x = I[x**x > y] = sum(I)/2
    return x

# print(super_rootv(10**9.5))


# 二分查找
# 问题1：给一个已经排序的数组，其中有N个互不相同的元素。要求使用最小的比较次数找出其中的一个元素。
def binary_search_1(array, key):
    l = 0
    r = len(array) - 1
    while l <= r:
        m = (l+r)//2
        if array[m] < key:
            l = m + 1
        elif array[m] > key:
            r = m - 1
        else:
            return m
    return -1

print(binary_search_1([1, 3, 5, 6, 7, 9, 10, 15], 3))

