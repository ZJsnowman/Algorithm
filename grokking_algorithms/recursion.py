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


if __name__ == '__main__':
    # countDown(25)
    # greet('Maggie')
    print(fact(5))
