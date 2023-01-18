class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            if nums[j] != val:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        return i