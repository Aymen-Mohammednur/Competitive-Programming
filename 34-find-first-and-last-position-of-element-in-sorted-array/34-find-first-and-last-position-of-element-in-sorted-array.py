class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        first = binarySearch(target)
        last = binarySearch(target + 1) - 1
        if first <= last:
            return [first, last]
        return [-1,-1]