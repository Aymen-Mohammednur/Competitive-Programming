class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = float('-inf')
        for num in nums:
            currSum += num
            if currSum < num:
                currSum = num
            maxSum = max(maxSum, currSum)
        return maxSum