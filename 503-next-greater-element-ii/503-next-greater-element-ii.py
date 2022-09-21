class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        for i in range((2 * len(nums)) - 1):
            while stack and nums[i % len(nums)] > stack[-1][0]:
                s = stack.pop()
                result[s[1]] = nums[i % len(nums)]
            stack.append((nums[i % len(nums)], i % len(nums)))
        return result