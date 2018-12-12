__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
import numpy as np


class Solution:
    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(A) <= 2: return len(A)
        prev = 1;
        curr = 2
        while curr < len(A):
            if A[curr] == A[prev] and A[curr] == A[prev - 1]:
                curr += 1
            else:
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1


if __name__ == '__main__':
    s = Solution()
    aList = [1, 1, 1, 2, 2, 3]
    bList = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    cList = []
    dList = [1, 2, 3]
    print(s.removeDuplicates(aList))
    print(s.removeDuplicates(bList))
    print(s.removeDuplicates(cList))
    print(s.removeDuplicates(dList))
