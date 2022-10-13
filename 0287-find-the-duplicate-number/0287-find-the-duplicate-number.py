class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def countLess(n):
            count = 0
            for i in nums:
                if i <= n:
                    count += 1
            return count
        l, r = 1, len(nums)
        while l <= r:
            mid = (l + r) // 2
            if countLess(mid) > mid:
                r = mid - 1
            else:
                l = mid + 1
        return l