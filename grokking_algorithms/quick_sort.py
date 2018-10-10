__author__ = 'ZJsnowman'


# -*- coding:utf-8 -*-


def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])


def mutli(aList):
    if len(aList) == 1:
        return aList[0]
    else:
        return aList[0] * mutli(aList[1:])


def len(list):
    if list == []:
        return 0
    else:
        return 1 + len(list[1:])




if __name__ == '__main__':
    print(sum([1, 2, 3]))
    print(mutli([2, 5, 6]))
    print(len([1, 1, 1, 1, 1]))
