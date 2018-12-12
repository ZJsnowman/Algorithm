__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np

# 如0-1背包问题：给定n种物品和一个背包。物品i的重量是Wi，其价值为Vi，背包的容量为C。应如何选择装入背包的物品，使得装入背包中的物品的总价值最大？
#
# 假设具体问题数值：A物品，重量为6kg，价值为8元，
#
#                 B物品，重量为8kg，价值为13元，
#
#                 C物品，重量为10kg，价值为15元
#
# 背包可以装为50kg的物品。
if __name__ == '__main__':
    beg = 50
    value = 0
    choise = []
    while beg > 0:
        if beg > 8:
            beg = beg - 8
            value = value + 13
            choise.append('B')
        elif beg > 10:
            beg = beg - 10
            value = value + 15
            choise.append('C')
        elif beg > 6:
            beg = beg - 6
            value = value + 8
            choise.append('A')
        else:
            break
    print(beg)
    print(value)
    print(choise)
