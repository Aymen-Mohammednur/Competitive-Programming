class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                mapping[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        result = []
        for n in nums1:
            if n in mapping:
                result.append(mapping[n])
            else:
                result.append(-1)
        return result