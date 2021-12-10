# LEETCODE 2089
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List

def targetIndices(self, nums: List[int], target: int):
        nums.sort()
        output = []
        for i in range(len(nums)):
            if (nums[i] == target):
                output.append(i)
        return output