__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = [i for i in nums if i != 0]
        for index, value in enumerate(temp):
            nums[index] = temp[index]
        for i in range(len(temp), len(nums)):
            nums[i] = 0

    def moveZeroes2(self, nums):
        k = 0
        for index, value in enumerate(nums):
            if nums[index]:
                nums[k], nums[index] = nums[index], nums[k]
                k = k + 1


if __name__ == '__main__':
    s = Solution()
    alist = [0, 1, 0, 3, 12]
    # s.moveZeroes(alist)
    s.moveZeroes2(alist)
    print(alist)
