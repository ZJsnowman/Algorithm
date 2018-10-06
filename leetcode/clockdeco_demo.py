import time
from leetcode.clock_decorator import clock
import functools


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@functools.lru_cache()
@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    snooze(.123)
    print('6!=', factorial(6))
    fibonacci(6)
