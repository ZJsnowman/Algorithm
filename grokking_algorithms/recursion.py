__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np


def countDown(x):
    if x < 0:
        return
    else:
        print(x)
        countDown(x - 1)


def greet2(name):
    print("how are you ,", name)


def bye():
    print('Ok,bye')


def greet(name):
    print("hello", name)
    greet2(name)
    print("getting ready to say bye")
    bye()


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


class DpFact:
    def __init__(self, n):
        self.mark = [0 for _ in range(0, n + 1)]
        print(self.fact(n))

    def fact(self, n):
        m = 0
        if self.mark[n] != 0:
            m = self.mark[n]
        elif n < 2:
            m = n

        else:
            m = fact(n - 1) + fact(n - 2)
        self.mark[n] = m
        return m


if __name__ == '__main__':
    # countDown(25)
    # greet('Maggie')
    # print(fact(1000000))
    DpFact(10)
