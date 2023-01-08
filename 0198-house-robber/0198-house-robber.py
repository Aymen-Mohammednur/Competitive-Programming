class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        return which houses you robbed
        '''
        # if len(nums) <= 1:
        #     return nums[0]
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # return dp[-1]
        
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i < 0:
                return 0
            pick = nums[i] + dp(i - 2)
            not_pick = dp(i - 1)
            memo[i] = max(pick, not_pick)
            return memo[i]
        return dp(len(nums) - 1)