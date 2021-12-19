# LEETCODE 1630
# https://leetcode.com/problems/arithmetic-subarrays/

from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        subArray = []
        output = []
        for i in range(len(l)):
            subArray = nums[l[i] : r[i]+1]
            subArray.sort()
            temp = subArray[1] - subArray[0]
            arithmetic = True
            for j in range(1, len(subArray) - 1):
                if (subArray[j+1] - subArray[j] != temp):
                    arithmetic = False
            output.append(arithmetic)
        return output
        