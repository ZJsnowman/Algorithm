__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    s = Solution()
    aList = [1, 1, 2]
    bList = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    cList = []
    print(s.removeDuplicates(aList))
    print(s.removeDuplicates(bList))
    print(s.removeDuplicates(cList))
