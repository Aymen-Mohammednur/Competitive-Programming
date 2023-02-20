class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = float('-inf')
        min_so_far = nums[0]
        for n in nums:
            max_diff = max(max_diff, n - min_so_far)
            min_so_far = min(min_so_far, n)
        return max_diff if max_diff != 0 else -1