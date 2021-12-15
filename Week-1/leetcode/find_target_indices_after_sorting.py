# LEETCODE 2089
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List

def targetIndices(nums: List[int], target: int):
    # nums.sort()
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if (nums[min_index] > nums[j]):
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        
    output = []
    for i in range(len(nums)):
        if (nums[i] == target):
            output.append(i)
    return output