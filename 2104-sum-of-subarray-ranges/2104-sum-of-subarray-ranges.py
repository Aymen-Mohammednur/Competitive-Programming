class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            Max, Min = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] >= Max:
                    Max = nums[j]
                if nums[j] <= Min:
                    Min = nums[j]
                result += Max - Min
        return result