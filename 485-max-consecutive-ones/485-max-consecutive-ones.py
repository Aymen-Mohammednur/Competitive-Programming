class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max = 0
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] == nums[fast] == 1:
                fast += 1
            else:
                slow = fast + 1
                fast = slow
            Max = max(Max, fast - slow)
        return Max