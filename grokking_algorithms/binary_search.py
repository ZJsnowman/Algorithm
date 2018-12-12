__author__ = 'ZJsnowman'


# -*- coding:utf-8 -*


def binary_search(aList, item):
    low = 0
    high = len(aList) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = aList[mid]
        if guess == item:
            return mid
        if guess > item:
            high = (mid - 1)
        else:
            low = (mid) + 1
    return None


def binary_search2(lst, item, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    guess = lst[mid]

    if item == guess:
        return mid  # 基线条件
    if item > guess:
        binary_search2(lst, item, mid + 1, high)  # 递归条件
    else:
        binary_search2(lst[:mid], item, low, mid - 1)


if __name__ == '__main__':
    my_list = [i for i in range(1, 10, 1)]
    print(my_list)
    # print(binary_search(my_list, 1))
    # print(binary_search(my_list, 5))
    # print(binary_search(my_list, -1))
    print(binary_search2(my_list, 1, 0, len(my_list) - 1))
    print(binary_search2(my_list, 5, 0, len(my_list) - 1))
    print(binary_search2(my_list, -1, 0, len(my_list) - 1))
