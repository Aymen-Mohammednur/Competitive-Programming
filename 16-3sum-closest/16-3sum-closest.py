class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if abs(target - currSum) < abs(target - closest):
                    closest = currSum
                if currSum < target:
                    left += 1
                elif currSum > target:
                    right -= 1
                else:
                    return target
        return closest