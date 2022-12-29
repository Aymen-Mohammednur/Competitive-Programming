class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = -1
        second_max = -1
        _max = 0
        for i in range(len(nums)):
            if nums[i] > _max:
                _max = nums[i]
                first_max = i
        _max = 0
        for i in range(len(nums)):
            if nums[i] > _max and i != first_max:
                _max = nums[i]
                second_max = i
        return (nums[first_max] - 1) * (nums[second_max] - 1)