# LEETCODE 229
# https://leetcode.com/problems/majority-element-ii/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        output = []
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for i in count:
            if count[i] > len(nums) / 3:
                output.append(i)
        return output