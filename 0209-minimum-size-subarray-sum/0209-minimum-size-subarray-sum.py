class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        l, r = 0, 0
        ans = float('inf')
        while l < len(nums):
            while currSum >= target:
                ans = min(ans, r - l)
                currSum -= nums[l]
                l += 1
            if r >= len(nums):
                break
            currSum += nums[r]
            r += 1
            if currSum >= target:
                ans = min(ans, r - l)
        return ans if ans != float('inf') else 0