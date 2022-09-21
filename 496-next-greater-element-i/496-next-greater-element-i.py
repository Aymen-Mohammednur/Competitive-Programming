class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        Dict = {}
        for n in nums2:
            while stack and n > stack[-1]:
                Dict[stack.pop()] = n
            stack.append(n)
            Dict[n] = -1
        result = []
        for n in nums1:
            result.append(Dict[n])
        return result