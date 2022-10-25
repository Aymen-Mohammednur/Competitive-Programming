class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        reached = 0
        # at every step check maximum index we can reach
        for i in range(n - 1):
            if i > reached:
                return False
            reached = max(reached, nums[i] + i)
            if reached >= n - 1:
                return True
        return False