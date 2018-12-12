__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np


# %%
def foo(x):
    print('x=', x)
    x = 200
    print('Changed in foo(), x = ', x)


if __name__ == '__main__':
    x = 100
    foo(x)
    print('x=', x)

# %%
y = 100


def foo1():
    print(y)


if __name__ == '__main__':
    foo1()

# %%
X = 100


def foo():
    global X
    print('foo() x = ', X)
    X = X + 5
    print('Changed in foo(), x = ', X)


def fun():
    global X
    print('fun() x = ', X)
    X = X + 1
    print('Changed in fun(), x = ', X)


if __name__ == '__main__':
    foo()
    fun()
    print('Result x = ', X)
