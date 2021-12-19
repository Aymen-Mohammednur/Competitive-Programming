# LEETCODE 1512
# https://leetcode.com/problems/number-of-good-pairs/
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numOfPairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] == nums[j] and i < j):
                    numOfPairs += 1
        return numOfPairs