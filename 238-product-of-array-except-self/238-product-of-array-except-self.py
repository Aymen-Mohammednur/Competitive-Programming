class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftToRight = [1]
        for i in range(len(nums)):
            leftToRight.append(leftToRight[-1] * nums[i])
        rightToLeft = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            rightToLeft[i] = rightToLeft[i + 1] * nums[i]
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = leftToRight[i] * rightToLeft[i + 1]
        return result