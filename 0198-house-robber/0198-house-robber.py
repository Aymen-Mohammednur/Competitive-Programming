class Solution:
    def rob(self, nums: List[int]):
        '''
        return which houses you robbed
        '''
        if len(nums) <= 1:
            return nums[0]
        dp = [0] * len(nums)
        robbed_houses = [None] * len(nums)
        dp[0] = nums[0]
        robbed_houses[0] = 0
        for i in range(1, len(nums)):
            if dp[i - 1] > dp[i - 2] + nums[i]:
                dp[i] = dp[i - 1]
                robbed_houses[i] = i - 1
                robbed_houses[i - 2] = None
            else:
                dp[i] = dp[i - 2] + nums[i]
                robbed_houses[i] = i
                robbed_houses[i - 1] = None
        # print(robbed_houses)
        return dp[-1]