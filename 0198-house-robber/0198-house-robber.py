class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[1], nums[0])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        # return dp[-1]
        memo = {}
        def td(index):
            if index in memo:
                return memo[index]
            if index >= len(nums):
                return 0
            pick = nums[index] + td(index + 2)
            not_pick = td(index + 1)
            
            memo[index] = max(pick, not_pick)
            return memo[index]
        return td(0)
    