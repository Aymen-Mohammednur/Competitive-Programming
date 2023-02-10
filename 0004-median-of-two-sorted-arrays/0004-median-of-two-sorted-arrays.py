class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        n = len(nums)
        nums.sort()
        if n % 2 != 0:
            return nums[n // 2]
        return (nums[n// 2] + nums[n // 2 - 1]) / 2