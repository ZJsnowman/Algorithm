__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np


def findSmallest(arr):
    """
    找出数组的最小值所在的索引
    :param arr: 数组
    :return: 索引
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == '__main__':
    aList = np.random.randint(1, 10, size=10).tolist()
    print(aList)
    print(selection_sort(aList))
