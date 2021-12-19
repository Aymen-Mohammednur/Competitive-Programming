# LEETCODE 1877
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pairs = []
        nums.sort()
        index = 0
        for i in range(len(nums) // 2):
            pairs.append([nums[index], nums.pop()])
            index += 1
        Max = sum(pairs[0])
        for i in range(1, len(pairs)):
            if (sum(pairs[i]) > Max):
                Max = sum(pairs[i])
        return Max