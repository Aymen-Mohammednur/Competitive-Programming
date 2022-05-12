class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for index, num in enumerate(nums):
            res ^= index
            res ^= num
        return res