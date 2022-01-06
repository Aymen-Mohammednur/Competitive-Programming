# LEETCODE 486
# https://leetcode.com/problems/predict-the-winner/

from typing import List

class Solution:
    def helper(self, start, end, nums):
        if start - end == 0:
            return nums[start]
        return max(nums[start] - self.helper(start + 1, end, nums), nums[end] - self.helper(start, end - 1, nums)) 

    def PredictTheWinner(self, nums: List[int]) -> bool:
        return True if self.helper(0, len(nums) - 1, nums) >= 0 else False
