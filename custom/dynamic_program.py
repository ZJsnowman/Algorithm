__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np
import time
from kits.time import clock


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


class DP(object):
    def __init__(self, n):
        self.mark = [0 for _ in range(n + 1)]
        print(self.dp(n))

    def dp(self, n):  # 递归的方法
        m = 0  # m的含义是当前n个台阶有m种跳法
        if self.mark[n] != 0:  # 先从备忘录寻找n，若存在mark[n]不等于0,则代表曾经计算过，n个台阶有mark[n]种跳法
            m = self.mark[n]  # 若备忘录有，则直接得到n层台阶的答案
        elif n <= 1:  # 从这里开始的四行是用来判断“边界问题”
            m = n
        elif n >= 2:  # 这里两行是用于规划转移方程式（其实这里很简单），青蛙只有两种可能，跳一层或者跳两层。
            m = self.dp(n - 2) + self.dp(n - 1)  # 当前n层台阶的解个数 等于 n-1层台阶的解 + n-2层台阶的解
        self.mark[n] = m  # 把m放入备忘录，下次若是再次是n层台阶，则不用计算直接取备忘录的数。（优化）
        return m


# coding=utf-8
class Dp2(object):
    def __init__(self, money):
        self.mark = [0 for _ in range(money + 1)]  # 备忘录
        print(self.dp(money))  # 开始递归

    def dp(self, money):
        self.coin = 0  # 需要的硬币数为0
        if self.mark[money] != 0:  # 在备忘录中寻找该金额下的最少硬币找零数，若存在，则取出
            self.coin = self.mark[money]
        elif money <= 0:  # 边界问题
            if money == 0:  # 如果金额为零，则代表刚好算是一种找零方法
                self.coin = 0  # 这里的0不是代表硬币数为0，而是代表这种方法可行，因为在下面已经有加1，若是这里coin为1，结果就会比答案多1
            else:
                self.coin = float("inf")  # 若是金额为负数，即“拿多了”，这种方法不可行，则硬币消耗数为 无穷大
        elif money > 0:
            self.coin = min(self.dp(money - 1), self.dp(money - 3), self.dp(money - 5)) + 1  # 递归，找出最少的可以凑齐金额数money的方法
        self.mark[money] = self.coin  # 做备忘录
        return self.coin





if __name__ == '__main__':
    start = time.time()
    # print(fib(30))
    # print(DP(30))
    dp2 = Dp2(65)  # 找零钱
    end = time.time()
    print(end - start)
