"""
利用动态规划的思想来解决斐波拉切数列
"""
import time


class DynimicFib(object):
    def __init__(self, n):
        self.num = 0
        self.mem = [-1 for _ in range(n + 1)]
        self.result = self.fib2(n)

    def fib(self, n):
        self.num += 1
        if n <= 1:
            return n
        if (self.mem[n] == -1):
            self.mem[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.mem[n]

    def fib2(self, n):
        self.mem[0] = 0
        self.mem[1] = 1
        for i in range(2, n + 1):
            self.mem[i] = self.mem[i - 1] + self.mem[i - 2]
        return self.mem[n]


if __name__ == '__main__':
    start = time.time()
    df = DynimicFib(10)

    print(df.result)
    end = time.time()
    print('num is ' + str(df.num))
    print('time is :' + str(end - start))
