class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
#         def td(index, picked):
#             if index >= len(nums):
#                 return 0
#             pick, not_pick = 0, 0
#             if picked:
#                 not_pick = td(index + 1, True)
#             else:
#                 pick = td(index + 1, False) + nums[index]
            
#             return max(pick, not_pick)
#         return td(0, True)
    