# LEETCODE 496
# https://leetcode.com/problems/next-greater-element-i/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        Dict = {}
        output = []
        
        for n in nums2:
            while stack and n > stack[-1]:
                Dict[stack.pop()] = n
            stack.append(n)
            
        while stack:
            Dict[stack.pop()] = -1
            
        for n in nums1:
            output.append(Dict[n])

        return output