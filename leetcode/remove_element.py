__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for value in nums:
            if value != val:
                nums[i] = value
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    print(s.removeElement(nums, 3))
    print(s.removeElement(nums2, 2))
