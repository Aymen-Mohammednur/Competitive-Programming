class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        numsSorted = deepcopy(nums)
        numsSorted.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != numsSorted[left] and nums[right] != numsSorted[right]:
                break
            if nums[left] == numsSorted[left]:
                left += 1
                count += 1
            elif nums[right] == numsSorted[right]:
                right -= 1
                count += 1
        return len(nums) - count