class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(nums, i, memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            pick = nums[i] + dp(nums, i + 2, memo)
            not_pick = dp(nums, i + 1, memo)
            memo[i] = max(pick, not_pick)
            return memo[i]
        case1 = nums[1:]
        case2 = nums[:len(nums) - 1]
        print(case1, case2)
        return max(dp(case1, 0, {}), dp(case2, 0, {}))