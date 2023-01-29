class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        l = 0
        res = 0
        nice = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                odd += 1
                nice = 0
            while odd >= k:
                
                odd -= nums[l] % 2
                l += 1
                nice += 1
                
            res += nice
        return res