__author__ = 'ZJsnowman'


# -*- coding:utf-8 -*-


class Solution:

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return self.sortColors(less) + [pivot] + self.sortColors(greater)


if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2, 0, 2, 1, 1, 0]))
