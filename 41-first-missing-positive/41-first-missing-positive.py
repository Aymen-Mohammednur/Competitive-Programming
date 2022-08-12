class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] - 1 != i and nums[i] > 0 and nums[i] < len(nums):
                if nums[i] == nums[nums[i] - 1]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] 
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1