class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) - 2, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        if i < 0:
            nums.reverse()
            return
        k = len(nums) - 1
        while nums[k] <= nums[i]:
            k -= 1
        nums[i], nums[k] = nums[k], nums[i]
        l, r = i + 1, len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1